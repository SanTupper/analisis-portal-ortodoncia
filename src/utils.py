from __future__ import annotations
import pandas as pd
import numpy as np

def cargar_clientes(path:str) -> pd.DataFrame:
    """Carga segura del CSV con tipos flexibles."""
    return pd.read_csv(path, low_memory=False)

def crear_kpis_pptos(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    # Evitar división por cero
    df['TicketPromPpto'] = np.where(df['CantPptos']>0, df['TotPptos']/df['CantPptos'], np.nan)
    # Cumplimiento: promedio simple de % abonados y % avanzados (ajustable)
    pct_abo = np.where(df['CantPptos']>0, df['CantPptosAbo']/df['CantPptos'], np.nan)
    pct_avan = np.where(df['CantPptos']>0, df['CantPptosAvan']/df['CantPptos'], np.nan)
    df['PctCumplimiento'] = np.nanmean(np.vstack([pct_abo, pct_avan]), axis=0)
    # Monto abonado promedio
    df['MontoAbonadoProm'] = np.where(df['CantPptosAbo']>0, df['TotPptosAbo']/df['CantPptosAbo'], np.nan)
    return df

def unificar_cobertura_salud(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    empresa = df.get('Empresa')
    isapre = df.get('ISAPRE')
    df['CoberturaSalud'] = np.where(empresa.notna() & (empresa.astype(str).str.len()>0), empresa, isapre)
    def map_cob(x):
        if pd.isna(x) or str(x).strip()=='' : return 'Desconocida'
        s = str(x).strip().upper()
        if 'FONASA' in s: return 'Fonasa'
        if 'ISAPRE' in s or s in {'CONSALUD','CRUZ BLANCA','MASVIDA','BANMEDICA','VIDA TRES','COLMENA'}: return 'Isapre'
        return 'Otra'
    df['CoberturaSaludCat'] = df['CoberturaSalud'].map(map_cob)
    return df

def marcar_activos(df: pd.DataFrame, dias_umbral:int=730) -> pd.Series:
    """Activo si tiene cualquier atención en ventanas recientes o días desde última visita <= umbral."""
    ventanas = [c for c in df.columns if c.lower().startswith('atencion')]
    cualquier_atencion = df[ventanas].fillna(0).sum(axis=1) > 0 if len(ventanas) else pd.Series(False, index=df.index)
    dias = pd.to_numeric(df.get('DiasDesdeUltimaVisita'), errors='coerce')
    por_dias = dias.le(dias_umbral).fillna(False)
    return (cualquier_atencion | por_dias)