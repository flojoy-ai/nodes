from flojoy import Image, flojoy, node_initialization
import serial


@flojoy(deps={"pyserial": "3.5"})
def LED_MATRIX_WS2812B(
    flojoy_init_input: serial.Serial, default: Image, port: str, width: int, height: int
) -> dict:
    """
    The LED_MATRIX_WS2812B node takes an image as an input and sends signals to the LED Matrix to light up specific
    LEDs accoring to the image input

    Parameters:
    - port: the port to which the LED Matrix is connected
    - width: the width of the LED Matrix
    - height: the height of the LED Matrix
    """
    input = default
    arduino = flojoy_init_input

    cmd = ""
    # Use the function to light up the LED
    for i in range(len(input.r)):
        for j in range(len(input.r[0])):
            # the LED matrix is a strand of LEDs that is folded into a matrix.
            # So, for a 5x5 LED, we have 25 LEDs in consecutive order, and after the 5th LED
            # on the first row, the 6th LED starts at the end of the second row, then after the 10th LED,
            # the 11th LED starts at the beginning of the third row, and so on. Here is a drawing of how the
            # LEDs are aligned:
            if input.r[i][j] == 0 and input.g[i][j] == 0 and input.b[i][j] == 0:
                continue

            led_position = i * width
            if i % 2 == 0:
                led_position += j
            else:
                led_position += width - j - 1

            cmd += f"{led_position},{input.r[i][j]},{input.g[i][j]},{input.b[i][j]},"

    arduino.write((cmd[:-1] + "\n").encode())
    return input  # return the input so that the next node can use it


@node_initialization(for_node=LED_MATRIX_WS2812B)
def start_serial_connection(port: str):
    arduino = serial.Serial(port, 115200)
    return arduino
