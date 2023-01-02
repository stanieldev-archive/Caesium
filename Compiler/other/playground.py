

















class Datatype:
    def __init__(self, token: str) -> None:
        self.dtype = None
        self.dsize = None
        self.is_pointer = False
        self.is_heap = False






def convert_to_datatype(token: str):
    is_pointer = False
    is_heap = False
    dtype = None

    if token[-1] == "^":
        is_pointer = True
        token = token[:-1]
        if token[0] == "[" and token[-1] == "]":
            is_heap = True
            token = token[1:-1]

        if token in datatype_set:
            self.datatype = token
        else:
            raise ValueError


















class Datatype:
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













parser_variables = {
    "auto",
	"bool",
	"char",
	"double",
	"enum",
	"float",
	"int",
	"long",
	"nullptr",
	"short",
	"struct",
	"typedef",
	"union",
	"void"
}




parser_keywords = {
    "break",
	"case",
	"continue",
	"default",
	"do",
	"else",
	"for",
	"goto",
	"if",
	"constexpr",
	"const",
	"false",
	"extern",
	"inline",
	"register",
	"restrict",
	"signed",
	"return",
	"static",
	"switch",
	"unsigned",
	"true",
	"volatile",
	"while"
}