from __future__ import annotations
import pandas as pd
import numpy as np

def cargar_clientes(path:str) -> pd.DataFrame:
    """Carga segura del CSV con tipos flexibles."""
    return pd.read_csv(path, low_memory=False)

def crear_kpis_pptos(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()

    # Asegurar numérico
    cols = ['CantPptos', 'TotPptos', 'CantPptosAbo', 'TotPptosAbo', 'CantPptosAvan', 'TotPptosAvan']
    for c in cols:
        if c in out.columns:
            out[c] = pd.to_numeric(out[c], errors='coerce')

    # Ticket promedio de ppto (si hay >0 presupuestos)
    out['TicketPromPpto'] = np.where(
        out.get('CantPptos', 0) > 0,
        out.get('TotPptos', np.nan) / out.get('CantPptos', np.nan),
        np.nan
    )

    # % de presupuestos abonados / avanzados (respecto del total de pptos)
    out['PctPptosAbonados'] = np.where(
        out.get('CantPptos', 0) > 0,
        out.get('CantPptosAbo', np.nan) / out.get('CantPptos', np.nan),
        np.nan
    )
    out['PctPptosAvanzados'] = np.where(
        out.get('CantPptos', 0) > 0,
        out.get('CantPptosAvan', np.nan) / out.get('CantPptos', np.nan),
        np.nan
    )

    # %Cumplimiento = promedio de los dos porcentajes (si ambos NaN, queda NaN)
    out['PctCumplimiento'] = out[['PctPptosAbonados', 'PctPptosAvanzados']].mean(axis=1, skipna=True)
    mask_ambos_nan = out[['PctPptosAbonados', 'PctPptosAvanzados']].isna().all(axis=1)
    out.loc[mask_ambos_nan, 'PctCumplimiento'] = np.nan

    # Monto abonado promedio (si hay >0 abonados)
    out['MontoAbonadoProm'] = np.where(
        out.get('CantPptosAbo', 0) > 0,
        out.get('TotPptosAbo', np.nan) / out.get('CantPptosAbo', np.nan),
        np.nan
    )

    return out

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