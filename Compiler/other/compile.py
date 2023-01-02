import argparse



















class Parser:

    def _console_args(self) -> dict:

        # Parser creation
        parser = argparse.ArgumentParser()

        # Positional arguments
        parser.add_argument("file", help="the file to compile", type=str)

        # Add arguments to console parser
        voice_group = parser.add_mutually_exclusive_group()
        voice_group.add_argument("-q", "--quiet", help="decreases debug output", action="store_true")
        voice_group.add_argument("-v", "--verbose", help="increases debug output", action="store_true")

        # Return arguments as dictionary
        return vars(parser.parse_args())

    def __init__(self) -> None:

        # Parser args
        console_args = self._console_args()

        # Final class arguments
        self.file_input = console_args["file"]
        self.file_output = console_args["file"] + ".cpp"
        self.bool_console_quiet = console_args["quiet"]
        self.bool_console_verbose = console_args["verbose"]

        # Parser variables
        self.bool_code_is_c = False
        self.bool_code_is_cpp = False
        self.default_bits_int = 32
        self.default_bits_float = 64

        # Parse file and print final file
        self._parse_file()

    


    def _parse_file(self) -> str:

        # Loop by line for converting to C++
        with open(self.file_output, "a+") as output_file:
            with open(self.file_input, "r") as input_file:
                for line_number, line in enumerate(input_file):
                    output_file.write(self._parse_line(line_number, line) + "\n")
                    
    def _parse_line(self, line: int, content: str) -> str:
        split_content = [i.strip("\n") for i in content.split(" ")]

        try:
            if split_content == ['']:
                return ""
            elif split_content[0] == "define":
                if split_content[2] != "as":
                    raise Exception(f"Invalid Variable Name on line {line}")
                return f"#define {split_content[1]} " + " ".join(split_content[3:])
            else:
                return str(split_content)
            
        except Exception as error:
            print(error)


# Concept



















def main() -> int:

    # Initialize parser
    caesium_parser = Parser()

    



    return 0



if __name__ == "__main__":
    main()