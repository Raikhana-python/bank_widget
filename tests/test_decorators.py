"""Тесты для декоратора log."""


import pytest

from src.decorators import log


class TestLogDecorator:
    """Тесты для декоратора log."""

    def test_log_to_console_success(self, capsys):
        """Логирование успешного выполнения в консоль."""
        @log()
        def add(a, b):
            return a + b

        result = add(2, 3)
        assert result == 5

        captured = capsys.readouterr()
        # Проверяем, что в логе есть имя функции и результат
        assert "add" in captured.err
        assert "5" in captured.err

    def test_log_to_console_error(self, capsys):
        """Логирование ошибки в консоль."""
        @log()
        def divide(a, b):
            return a / b

        with pytest.raises(ZeroDivisionError):
            divide(10, 0)

        captured = capsys.readouterr()
        assert "divide" in captured.err
        assert "ERROR: ZeroDivisionError" in captured.err
        assert "10, 0" in captured.err

    def test_log_to_file_success(self, tmp_path):
        """Логирование успешного выполнения в файл."""
        log_file = tmp_path / "test.log"

        @log(filename=str(log_file))
        def multiply(a, b):
            return a * b

        result = multiply(4, 5)
        assert result == 20

        # Проверяем содержимое файла
        assert log_file.exists()
        content = log_file.read_text()
        assert "multiply" in content
        assert "20" in content
        assert "4, 5" in content

    def test_log_to_file_error(self, tmp_path):
        """Логирование ошибки в файл."""
        log_file = tmp_path / "test_error.log"

        @log(filename=str(log_file))
        def divide(a, b):
            return a / b

        with pytest.raises(ZeroDivisionError):
            divide(10, 0)

        assert log_file.exists()
        content = log_file.read_text()
        assert "divide" in content
        assert "ERROR: ZeroDivisionError" in content
        assert "10, 0" in content

    def test_log_with_kwargs(self, capsys):
        """Логирование с именованными аргументами."""
        @log()
        def greet(name, greeting="Hello"):
            return f"{greeting}, {name}!"

        result = greet("Alice", greeting="Hi")
        assert result == "Hi, Alice!"

        captured = capsys.readouterr()
        assert "greet" in captured.err
        assert "Hi, Alice!" in captured.err
        # Проверяем, что kwargs отображаются в логе
        assert "greeting='Hi'" in captured.err

    def test_log_different_functions(self, capsys):
        """Логирование двух разных функций."""
        @log()
        def square(x):
            return x ** 2

        @log()
        def cube(x):
            return x ** 3

        square(2)
        cube(3)
        captured = capsys.readouterr()
        assert "square" in captured.err
        assert "cube" in captured.err
