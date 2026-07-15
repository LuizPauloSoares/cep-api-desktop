#importação
import requests
import sys
from PyQt5.QtWidgets import QApplication , QWidget,QLabel,QPushButton,QLineEdit,QMessageBox

def cadastro():
    usuario = caixaTextoNome.text()
    QMessageBox.information(janela, "cadastrado", f"seja bem vindo {usuario}") 

def validaCampos():

    if len(caixaTextoCpf.text()) != 11:
         QMessageBox.critical(janela , "Atenção" , "CPF invalido")
         caixaTextoCpf.setFocus()

    elif len(caixaTextoNome.text()) <3:
         QMessageBox.critical(janela, "Atenção" , "nome invalido")
         caixaTextoNome.setFocus()

    elif len(caixaTextoRg.text()) <7 or len(caixaTextoRg.text()) >11:
        QMessageBox.critical(janela, "Atenção" , "Rg invalido")
        caixaTextoRg.setFocus()

    elif len(caixaTextoMae.text()) <3:
        QMessageBox.critical(janela, "Atenção" , "nome invalido")
        caixaTextoMae.setFocus()
    else:
         cadastro()

#limpa campos 
def limpaCampos():
    #funçao para limpar campos e posicionar o cursor no campo cpf
    caixaTextoNome.clear()
    caixaTextoCpf.clear()
    caixaTextoRg.clear()
    caixaTextoNascimento.clear()#valida 
    caixaTextoMae.clear()
    caixaTextoCep.clear()
    caixaTextoLogradouro.clear()
    caixaTextoBairro.clear()
    caixaTextoCidade.clear()
    caixaTextoUf.clear()
    caixaTextoCep.setFocus()

#funçao para validar o campo cep
def validaCep ():
    
    #variavelq guarda o cep informado
    codigoCep = caixaTextoCep.text()

    if codigoCep == "":
         QMessageBox.critical(janela, "Atenção" , "Cep invalido")
    else:
         #chama outra finçao pra verificar o cep
         tratarCep(codigoCep)

def tratarCep (codigoCep):
    url = f"https://viacep.com.br/ws/{codigoCep}/json/"

    try:
        response = requests.get(url)
        
        #verifica o resultado          
        if response.status_code == 200:
            dados = response.json()

             #verifica se a chave "erro" existe e se o valor e true
            if dados.get("erro") == "true":
                    QMessageBox.critical(janela, "Atenção" , "lcep nao encontrado ")
            else:
                caixaTextoLogradouro.setText(dados.get('logradouro', ''))
                caixaTextoBairro.setText(dados.get('bairro',''))
                caixaTextoCidade.setText(dados.get('localidade',''))
                caixaTextoUf.setText(dados.get('uf','')) 
                
                QMessageBox.information(janela , "consulta de cep", "endereço encontrado")

        else:
             QMessageBox.critical(janela, "erro" , f"erro na requisiçao codigo de estatos {response.status_code}")        

    except:
           QMessageBox.critical(janela, "erro" , f"ocorreu uma exceção: {str(e)}")


# criando a aplicação
app = QApplication(sys.argv)

janela = QWidget()
janela.setWindowTitle("Verificação de CEP")
janela.setGeometry(725, 300, 560, 600)  # altura aumentada para acomodar os novos Y

#    Labels 
# label nome 
textoRotuloNome = QLabel("Nome completo ", janela)
textoRotuloNome.move(40, 30)

# label CPF
textoRotuloCpf = QLabel("Cpf" , janela)
textoRotuloCpf.move(40, 70)

# label Rg
textoRotuloRg = QLabel("Rg" , janela)
textoRotuloRg.move(40, 110)

# label data nascimento
textoRotuloNascimento = QLabel("Data  nascimento" ,janela)
textoRotuloNascimento.move(40, 150)

# label nome mae 
textoRotuloMae = QLabel("nome da mae" ,janela)
textoRotuloMae.move(40, 190)

# CEP
textoRotuloCep = QLabel("CEP", janela)
textoRotuloCep.move(40, 230)

# Logradouro
textoRotuloLogradouro = QLabel("Logradouro", janela)
textoRotuloLogradouro.move(40, 270)

# Número
textoRotuloNumero = QLabel("Número", janela)
textoRotuloNumero.move(40, 310)

# label Complemento
textoRotuloComplemento = QLabel("Complemento" ,janela)
textoRotuloComplemento.move(40, 350)

# Bairro (reposicionado para manter espaçamento)
textoRotuloBairro = QLabel("Bairro", janela)
textoRotuloBairro.move(40, 390)

# Cidade (reposicionado)
textoRotuloCidade = QLabel("Cidade", janela)
textoRotuloCidade.move(40, 430)

# UF (reposicionado)
textoRotuloUf = QLabel("UF", janela)
textoRotuloUf.move(40, 470)

#   Campos de texto 

# nome
caixaTextoNome = QLineEdit(janela)
caixaTextoNome.move(160, 30)      
caixaTextoNome.resize(250, 25)

# cpf
caixaTextoCpf = QLineEdit(janela)
caixaTextoCpf.move(160, 70)   
caixaTextoCpf.resize(150, 25)

# rg
caixaTextoRg = QLineEdit(janela)
caixaTextoRg.move(160, 110)       
caixaTextoRg.resize(150, 25)

# nascimento
caixaTextoNascimento = QLineEdit(janela)
caixaTextoNascimento.move(160, 150)   
caixaTextoNascimento.resize(120, 25)

# mae
caixaTextoMae = QLineEdit(janela)
caixaTextoMae.move(160, 190)
caixaTextoMae.resize(250, 25)

# CEP
caixaTextoCep = QLineEdit(janela)
caixaTextoCep.move(160, 230)
caixaTextoCep.resize(300, 25)
caixaTextoCep.setInputMask("00000-000")
caixaTextoCep.returnPressed.connect(validaCep)

# Logradouro
caixaTextoLogradouro = QLineEdit(janela)
caixaTextoLogradouro.move(160, 270)
caixaTextoLogradouro.resize(300, 25)
caixaTextoLogradouro.setEnabled(False)

# Número
caixaTextoNumero = QLineEdit(janela)
caixaTextoNumero.move(160, 310)
caixaTextoNumero.resize(100, 25)

# Complemento
caixaTextoComplemento = QLineEdit(janela)
caixaTextoComplemento.move(160, 350)
caixaTextoComplemento.resize(180, 25)

# Bairro (reposicionado)
caixaTextoBairro = QLineEdit(janela)
caixaTextoBairro.move(160, 390)
caixaTextoBairro.resize(300, 25)
caixaTextoBairro.setEnabled(False)

# Cidade (reposicionado)
caixaTextoCidade = QLineEdit(janela)
caixaTextoCidade.move(160, 430)
caixaTextoCidade.resize(300, 25)
caixaTextoCidade.setEnabled(False)

# UF (reposicionado)
caixaTextoUf = QLineEdit(janela)
caixaTextoUf.move(160, 470)
caixaTextoUf.resize(50, 25)
caixaTextoUf.setEnabled(False)

# Botões (reposicionados)
btnLimpar = QPushButton("Limpar", janela)
btnLimpar.move(160, 510)
btnLimpar.resize(100, 30)
btnLimpar.clicked.connect(limpaCampos)


btnCadastrar = QPushButton("cadastrar", janela)
btnCadastrar.move(280, 510)
btnCadastrar.resize(120, 30)
btnCadastrar.clicked.connect(validaCampos)

# exibindo a janela 
janela.show()

# iniciando o loop de eventos 
sys.exit(app.exec_())
