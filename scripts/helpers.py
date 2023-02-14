
def create_outputdir(path: str="test") -> bool:
    if not os.path.exists(path):
       os.makedirs(path)
       return True
    return False
