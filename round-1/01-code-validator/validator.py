import unittest

def is_valid_access_code(code):
    """Return whether code is a valid six digit student access code."""
    try:

        if isinstance(code,int):

            return False

        if code(0) != '0':

            return False


        if len(code)==6:
            code_checker = int(code)

            for i in range(len(code)):

                if code(i) not int:

                    return False

                i=+1

            return True

        return False

                
                

    
            

    


    

    


    

            

            

        




       # this line is non functional, it converts the code into an int and then into a String
       # return len(str(int(code))) == 6


    
    except (TypeError, ValueError):
        return False


class ValidatorTests(unittest.TestCase):
    def test_six_digit_code_is_valid(self):
        self.assertTrue(is_valid_access_code("123456"))

    def test_leading_zero_code_is_valid(self):
        self.assertTrue(is_valid_access_code("001234"))

    def test_non_digit_code_is_invalid(self):
        self.assertFalse(is_valid_access_code("12a456"))

    def test_non_ascii_digits_are_invalid(self):
        self.assertFalse(is_valid_access_code("１２３４５６"))

    def test_unrelated_arithmetic(self):
        self.assertEqual(2 + 2, 4)


if __name__ == "__main__":
    unittest.main()
