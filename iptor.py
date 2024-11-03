from stem.descriptor.remote import DescriptorDownloader

# Descargar el consenso de Tor
downloader = DescriptorDownloader()
print("Descargando el documento de consenso de Tor...")

try:
    consensus = downloader.get_consensus().run()
    print("Documento de consenso descargado con éxito.")
except Exception as e:
    print("Error al descargar el documento de consenso:", e)
    exit(1)

# Procesar y listar los nodos directamente sin usar parse_file
print("Lista de nodos de Tor:")
for descriptor in consensus:
    # Cada descriptor tiene mucha información; aquí mostramos algunos campos clave
    print(f"Nombre del nodo: {descriptor.nickname}")
    print(f"Dirección IP: {descriptor.address}")
    print(f"Puerto OR: {descriptor.or_port}")
    print(f"Flags: {', '.join(descriptor.flags)}")
    print("-" * 40)
