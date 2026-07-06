def formata_titulo(titulo: str) -> str:
    """Formata um título com linhas de destaque."""
    linha = "=" * len(titulo)
    return f"{titulo}\n{linha}"
