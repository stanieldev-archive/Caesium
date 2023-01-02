





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







COMPILER_KEYWORDS = {"define", "include", "//", "[C++>", "<C++]", "[C>", "<C]"}
PARSER_KEYWORDS = {}
DATATYPE_KEYWORDS = {"int", "float", "char", "bool", "void"}



class CeType:
    dtype = ""
    dsize = 0
    dvalue = None

    is_unsigned = False
    is_pointer = False

integer_type = CeType()
integer_type.dtype = "int"
integer_type.dsize = 64
integer_type.is_pointer = False
integer_type.is_unsigned = False










        






class Parser:
    def __init__(self, file: str):

        # Required items
        self.input_file = file
        self.output_file = file[:-3] + ".cpp"

        # Parser settings
        self.save_comments = False
        self.allow_lang_c = False
        self.allow_lang_cpp = False

        # Internal states
        self.is_comment = False
        self.is_lang_c = False
        self.is_lang_cpp = False


    def run_through_file(self) -> str:
        with open(self.output_file, "a+") as output_file:
            with open(self.input_file, "r") as input_file:
                for line in input_file:
                    formatted = self.parse(line.strip())
                    if formatted != "":
                        output_file.write(formatted + "\n")




    # def multi_comment(self, content: str) -> str:
    #     BEGIN_COMMENT = "/*"
    #     END_COMMENT = "*/"

    #     if self.is_comment:
    #         if END_COMMENT in content:
    #             self.is_comment = False
    #             content = content.replace(END_COMMENT, "*/", 1)  # C-style comment
    #         return content if self.save_comments else ""
        
    #     elif BEGIN_COMMENT in content:
    #         self.is_comment = True
    #         split_index = content.index(BEGIN_COMMENT)
    #         content = content.replace(BEGIN_COMMENT, "/*", 1)
    #         code = content[:split_index]
    #         comment = content[split_index:] if self.save_comments else ""
    #         return self.parse(code) + comment
        
    #     return False


    # def single_comment()





    def parse(self, content: str) -> str:
        content = content.strip()

        # Multi-line comment
        if self.is_comment:
            if "*/" in content:
                self.is_comment = False
                content = content.replace("*/", "*/", 1)
            return content if self.save_comments else ""
        elif not self.is_comment and "/*" in content:
            self.is_comment = True
            split_index = content.index("/*")
            content = content.replace("/*", "/*", 1)
            code = content[:split_index]
            comment = content[split_index:] if self.save_comments else ""
            return self.parse(code) + comment

        # C-Style Transpile comment
        elif self.is_lang_c:
            if "<C]" in content:
                self.is_lang_c = False
                content = content.replace("<C]", "", 1)
            return content if self.allow_lang_c else ""
        elif not self.is_lang_c and "[C>" in content:
            self.is_lang_c = True
            split_index = content.index("[C>")
            content = content.replace("[C>", "", 1)
            code = content[:split_index]
            comment = content[split_index:] if self.allow_lang_c else ""
            return self.parse(code) + comment

        # C++ Style Transpile comment
        elif self.is_lang_cpp:
            if "<C++]" in content:
                self.is_lang_cpp = False
                content = content.replace("<C++]", "", 1)
            return content if self.allow_lang_cpp else ""
        elif not self.is_lang_cpp and "[C++>" in content:
            self.is_lang_cpp = True
            split_index = content.index("[C++>")
            content = content.replace("[C++>", "", 1)
            code = content[:split_index]
            comment = content[split_index:] if self.allow_lang_cpp else ""
            return self.parse(code) + comment

        # Single-line comment
        if "//" in content:
            split_index = content.index("//")
            content = content.replace("//", "//", 1)
            code = content[:split_index]
            comment = content[split_index:] if self.save_comments else ""
            return self.parse(code) + comment




        return content













def main():
    parser = Parser(file="syntax_testing.ce")
    parser.run_through_file()



if __name__ == "__main__":
    main()
