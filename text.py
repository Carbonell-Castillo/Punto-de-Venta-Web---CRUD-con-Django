import xml.etree.ElementTree as ET
import xml.dom.minidom


def leerEntrada(xml_file):
    try:
        tree = ET.parse(xml_file)
    except Exception as e:
        print("Error al leer el archivo de entrada: ", e)

    root = tree.getroot()

    facturas = []
    productosObtenidos = []
    clientesObtenidos = []
    for factura in root.findall('factura'):
        numero = factura.find('numero').text
        print(numero)
        for cliente in factura.findall('cliente'):
            nit = cliente.find('nit').text
            nombre = cliente.find('nombre').text
            direccion = cliente.find('direccion').text
            print(nit, nombre, direccion)
            clientesObtenido = {
                "nit": nit,
                "nombre": nombre,
                "direccion": direccion
            }
            clientesObtenidos.append(clientesObtenido)
        for productos in factura.findall('productos'):
            for producto in productos.findall('producto'):
                nombre = producto.find('nombre').text
                precio = producto.find('precio').text
                stock = producto.find('stock').text
                descripcion = producto.find('descripcion').text
                productosObtenido = {
                    "nombre": nombre,
                    "precio": precio,
                    "stock": stock,
                    "descripcion": descripcion
                }
                productosObtenidos.append(productosObtenido)
                
            
                print(nombre, precio, stock)
                
        facturas.append([numero, clientesObtenidos, productosObtenidos])

    return facturas
        
def escribir_xml(xml_file, facturas):
    root = ET.Element("facturas")
    for factura in facturas:
        factura_xml = ET.SubElement(root, "factura")
        numero = ET.SubElement(factura_xml, "numero")
        numero.text = factura[0]
        cliente = ET.SubElement(factura_xml, "cliente")
        nit = ET.SubElement(cliente, "nit")
        nit.text = factura[1][0]["nit"]
        nombre = ET.SubElement(cliente, "nombre")
        nombre.text = factura[1][0]["nombre"]
        direccion = ET.SubElement(cliente, "direccion")
        direccion.text = factura[1][0]["direccion"]
        productos = ET.SubElement(factura_xml, "productos")
        for producto in factura[2]:
            producto_xml = ET.SubElement(productos, "producto")
            nombre = ET.SubElement(producto_xml, "nombre")
            nombre.text = producto["nombre"]
            precio = ET.SubElement(producto_xml, "precio")
            precio.text = producto["precio"]
            stock = ET.SubElement(producto_xml, "stock")
            stock.text = producto["stock"]
            descripcion = ET.SubElement(producto_xml, "descripcion")
            descripcion.text = producto["descripcion"]
    tree = ET.ElementTree(root)
    with open("factura2.xml", "wb") as xml_file:
        tree.write(xml_file, encoding="utf-8", xml_declaration=True, method="xml")
        indent_xml_file(xml_file)

def indent_xml_file(xml_file):

    with open(xml_file.name, "rb") as f:
        content = f.read()


    dom = xml.dom.minidom.parseString(content)
    indented_content = dom.toprettyxml(encoding="utf-8")


    with open(xml_file.name, "wb") as f:
        f.write(indented_content)


ruta_archivo = "IPC2_PROYECTO2/factura.xml"
factura = leerEntrada(ruta_archivo)
print(factura)
escribir_xml("factura2.xml", factura)
#Obtener el numero de la factura del ultimo

numeroFactura = factura[-1][0]
print(numeroFactura)

