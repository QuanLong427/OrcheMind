import tomllib


def test_pyproject_exposes_orchemind_console_script() -> None:
    with open("pyproject.toml", "rb") as file:
        pyproject = tomllib.load(file)

    assert pyproject["project"]["scripts"]["orchemind"] == "orchemind.backend.app.cli.main:main"
