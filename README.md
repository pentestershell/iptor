# iptor
Este script descarga el consenso y luego muestra una lista de los nodos de la red Tor
Explicación del Script

    Descarga del consenso: Utiliza DescriptorDownloader de stem.descriptor.remote para obtener el consenso directamente desde la red Tor.
    Parsing del archivo: Usa parse_file de stem.descriptor para interpretar el archivo de consenso y extraer los detalles de cada nodo.
    Información de cada nodo: Extrae y muestra el nombre, IP, puerto OR (donde el nodo acepta conexiones), y los flags que indican el tipo de nodo (por ejemplo, Guard, Exit, Authority).

Campos adicionales

El archivo de consenso contiene otros campos interesantes, como la cantidad de ancho de banda disponible de cada nodo, la huella dactilar (fingerprint), etc. Puedes acceder a estos campos desde el descriptor y agregar más detalles en la impresión si te resulta útil.

Este script debería funcionar siempre que el documento de consenso esté disponible y actualizado.
