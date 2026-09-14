"""Ponto de entrada principal do LUMPT."""

from __future__ import annotations


def main() -> None:
    try:
        import tkinter  # noqa: F401
    except ModuleNotFoundError as exc:
        if exc.name == "tkinter":
            raise SystemExit(
                "Não consegui abrir a interface.\n\n"
                "Reinstale o Python com Tcl/Tk habilitado ou verifique a instalação do \n"
                "intérprete do Windows."
            ) from exc
        raise

    from lumpt.app import run

    run()


if __name__ == "__main__":
    main()