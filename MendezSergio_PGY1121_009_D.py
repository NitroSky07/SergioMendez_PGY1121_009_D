import funciones as fn

while True:
    fn.ver_menu()
    opcion= fn.validar_opcion()
    if opcion==1:
        fn.ver_menu()
        fn.comprar_entradas()
    elif opcion==2:
        fn.mostrar_ubicaciones()
    elif opcion==3:
        pass
    elif opcion==4:
        fn.ganancias()
    else:
        break