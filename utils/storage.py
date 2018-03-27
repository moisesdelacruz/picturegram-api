# funcion para almacenamiento de imagenes
def content_file_name(instance, filename):
    content = str(instance.__class__.__name__).lower() + 's'
    return '/'.join([content, str(instance), filename])