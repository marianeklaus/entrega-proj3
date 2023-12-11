import es
import design

funcao = es.leitor_funcao()

if funcao == "1" or funcao == "2":
    coeficientes = es.leitor_coeficiente(funcao)
else: 
    coeficientes = []

pontos = design.design(funcao, coeficientes)

es.impressora(pontos)

if __name__=="__main__":
    main()