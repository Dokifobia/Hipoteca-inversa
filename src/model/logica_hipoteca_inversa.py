# excepciones personalizadas para la logica de hipoteca inversa
class ValorPropiedadCero(Exception):
    """Se dispara cuando el valor de la propiedad es 0."""
    pass


class HipotecaUsura(Exception):
    """Se dispara cuando la tasa mensual supera el límite permitido."""
    pass


class PlazoMayorPermitido(Exception):
    """Se dispara cuando el plazo de meses es mayor al máximo permitido."""
    pass


class PlazoMenorIgualCero(Exception):
    """Se dispara cuando el plazo de meses es menor o igual a 0."""
    pass



# Constantes de negocio (valores inmutables)
TASA_MAXIMA_USURA: float = 0.04
PLAZO_MAXIMO_MESES: int = 240
PLAZO_MINIMO_MESES: int = 1

# logica hipoteca inversa
def desembolso_mensual(
    valor_inmueble: float,
    porcentaje: float,
    tasa_mensual: float,
    plazo_meses: int
) -> tuple[float, float, float]:


    validar_parametros(valor_inmueble, tasa_mensual, plazo_meses)

    monto_prestamo = valor_inmueble * porcentaje
    tasa = tasa_mensual
    plazo = plazo_meses

    if tasa == 0:
        cuota_mensual = monto_prestamo / plazo
    else:
        cuota_mensual = (monto_prestamo * tasa) / (1 - (1 + tasa) ** -plazo)

    total_abonos = cuota_mensual * plazo
    total_intereses = total_abonos - monto_prestamo

    return cuota_mensual, total_abonos, total_intereses


def validar_parametros(valor_inmueble: float, tasa_mensual: float, plazo_meses: int) -> None:

    if valor_inmueble <= 0:
        raise ValorPropiedadCero("El valor del inmueble debe ser mayor que cero.")

    if tasa_mensual > TASA_MAXIMA_USURA:
        raise HipotecaUsura(
            f"La tasa mensual supera el máximo permitido ({TASA_MAXIMA_USURA*100:.0f}%)."
        )

    if plazo_meses > PLAZO_MAXIMO_MESES:
        raise PlazoMayorPermitido(
            f"El plazo no debe ser mayor a {PLAZO_MAXIMO_MESES} meses."
        )

    if plazo_meses < PLAZO_MINIMO_MESES:
        raise PlazoMenorIgualCero(
            f"El plazo debe estar entre {PLAZO_MINIMO_MESES} y {PLAZO_MAXIMO_MESES} meses."
        )
