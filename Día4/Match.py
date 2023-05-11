serie = 'N-02'
match serie:
    case 'N-01':
        print('SAMSUNG')
    case 'N-02':
        print('Nokia')
    case 'N-03':
        print('Motorola')
    case 'N-04':
        print('Apple')
    case 'N-05':
        print

cliente = {'nombre':'federico',
           'edad':45,
           'ocupacion':'instructor'}
pelicula = {'titulo':'matrix',
            'ficha_tecnica': {'protagonista':'keanu reeves',
                             'director':'lana y lilly wachowsky'}
}
elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre':nombre,
              'edad':edad,
              'ocupacion':ocupacion}:
            print("Es un cliente")
            print(nombre, edad, ocupacion)
        case _:
            print('no hay')







