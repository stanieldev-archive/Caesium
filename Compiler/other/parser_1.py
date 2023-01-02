


keyword_set = {"return", "define", "as", "in"}
datatype_set = {"float32", "float64", "int32", "int64", "int128", "char", "iint64", "cint8"}





class DataType:
    def __init__(self, token: str) -> None:
        self.datatype = None
        self.is_pointer = False
        self.is_heap = False
        self._convert_to_datatype(token)

    def __repr__(self) -> str:
        return f"Datatype( Datatype: {self.datatype}, is_pointer: {self.is_pointer}, is_heap: {self.is_heap} )"

    def _convert_to_datatype(self, token: str) -> None:
        if token[-1] == "^":
            self.is_pointer = True
            token = token[:-1]
        if token[0] == "[" and token[-1] == "]":
            self.is_heap = True
            token = token[1:-1]

        if token in datatype_set:
            self.datatype = token
        else:
            raise ValueError



class DataTypeM:
    def __init__(self, token: str) -> None:
        self.datatype = None
        self.is_pointer = False
        self.is_heap = False
        self._convert_to_datatype(token)

    def __repr__(self) -> str:
        return f"Datatype( Datatype: {self.datatype}, is_pointer: {self.is_pointer}, is_heap: {self.is_heap} )"

    def _convert_to_datatype(self, token: str) -> None:
        if token[-1] == "^":
            self.is_pointer = True
            token = token[:-1]
        if token[0] == "[" and token[-1] == "]":
            self.is_heap = True
            token = token[1:-1]
        self.datatype = DataType(token)












class Parser:
    def __init__(self) -> None:
        self.file_input = "input.ce"
        self.file_output = "input.cpp"
        self._parse()

    def _parse(self) -> str:
        line_number = 1
        with open(self.file_output, "a+") as output_file:
            with open(self.file_input, "r") as input_file:
                for line in input_file:

                    try:
                        converted = self._convert(line)
                    except ValueError:
                        print(f"Line {line_number}: Failed to convert line.")
                        return
                        
                    if converted is not None:
                        output_file.write(converted + "\n")
                    line_number += 1

    def _convert(self, token: str) -> str:
        return token.strip("\n")










    # def _parse_line(self, line_number: int, line_content: str) -> str:
    #     tokens = line_content.strip("\n").split(" ")
    #     tokens = [i for i in tokens if i != ""]
    #     if tokens == [""] or tokens == []: return

    #     output_list = []
    #     for token in tokens:
    #         output_list.append(str(self._token_conversion(token)))
            
    #     return " ".join(output_list)

    # def _token_conversion(self, token: str) -> str:

    #     # If token is a keyword
    #     if token in keyword_set:
    #         return token

    #     # If token is a datatype
    #     is_datatype = False
    #     for i in datatype_set:
    #         if i in token:
    #             is_datatype = True
    #             break
    #     if is_datatype:
    #         return DataType(token)













    #     return token









def main() -> None:
    Parser()

if __name__ == "__main__":
    main()