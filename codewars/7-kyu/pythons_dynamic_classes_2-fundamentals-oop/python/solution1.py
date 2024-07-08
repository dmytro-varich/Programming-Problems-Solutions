class ReNameAbleClass(object):
    
    @classmethod
    def change_class_name(cls, new_name):
        assert new_name[0].isupper() and new_name.isalnum()
        cls.__name__ = new_name
            
    @classmethod
    def __str__(cls):
        return f"Class name is: {cls.__name__}"
