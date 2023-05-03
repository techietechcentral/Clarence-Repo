
class Temperature:
    """
    A class for handling temperature conversion and validation.

    Attributes:
        temp_celsius (float): The temperature in degrees Celsius.

    Methods:
        convert_temp_to_fahrenheit(): Converts the temperature from Celsius to Fahrenheit.
        convert_fahrenheit_to_cel(temp_fah): Converts the temperature from Fahrenheit to Celsius.
        check_valid_temp(temp): Checks if the temperature is within a valid range.
        create_with_fahrenheit(cls, temperature): Creates a Temperature object from a temperature in Fahrenheit.
        standard(cls): Creates a Temperature object with a temperature of 0 degrees Celsius.
        __repr__(): Returns a string representation of the Temperature object.
    """

    def __init__(self, temp_celsius: float):
        """
        Initializes the Temperature object with a temperature in degrees Celsius.

        Args:
            temp_celsius (float): The temperature in degrees Celsius.
        """
        self.temp_celsius = temp_celsius

    def convert_temp_to_fahrenheit(self) -> float:
        """
        Converts the temperature from Celsius to Fahrenheit.

        Returns:float: The temperature in degrees Fahrenheit.
        """
        return (self.temp_celsius * 1.8) + 32

    @staticmethod
    def convert_fahrenheit_to_cel(temp_fah: float) -> float:
        """
        Converts the temperature from Fahrenheit to Celsius.

        Args:
            temp_fah (float): The temperature in degrees Fahrenheit.

        Returns:
            float: The temperature in degrees Celsius.
        """
        return (temp_fah - 32) * 1.8

    @staticmethod
    def check_valid_temp(temp: float) -> None:
        """
        Checks if the temperature is within a valid range.

        Args:
            temp (float): The temperature to check.

        Returns:
            None
        """
        if -273 <= temp <= 3000:
            print("This is a valid temperature")

    @classmethod
    def create_with_fahrenheit(cls, temperature: float) -> 'Temperature':
        """
        Creates a Temperature object from a temperature in Fahrenheit.

        Args:
            temperature (float): The temperature in degrees Fahrenheit.

        Returns:
            Temperature: A Temperature object with the converted temperature in degrees Celsius.
        """
        return cls(Temperature.convert_fahrenheit_to_cel(temperature))

    @classmethod
    def standard(cls) -> 'Temperature':
        """
        Creates a Temperature object with a temperature of 0 degrees Celsius.

        Returns:
            Temperature: A Temperature object with a temperature of 0 degrees Celsius.
        """
        return cls(0)

    def __repr__(self) -> str:
        """
        Returns a string representation of the Temperature object.

        Returns:
            str: A string representation of the Temperature object.
        """
        temp = str(self.temp_celsius)
        return temp