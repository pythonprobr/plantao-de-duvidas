_usuarios = {'renzo@python.pro.br': 'Renzo Nuccitelli'}


class BancoDeDadosException(Exception):
    pass


class UsuarioNaoEncontrado(BancoDeDadosException):
    pass


class EmailInvalido(BancoDeDadosException):
    def __init__(self, msg_de_erro: str, email: str) -> None:
        super().__init__()
        self.email = email
        self.msg_de_erro = msg_de_erro


def procurar_usuario_no_banco(email: str) -> str:
    if '@' not in email:
        raise EmailInvalido('Email inválido, faltando caracter "@"', email)
    try:
        return _usuarios[email]
    except KeyError as e:
        print('Deu ruim no banco')
        raise UsuarioNaoEncontrado() from e


def enviar_email_de_boas_vindas(email: str) -> None:
    try:
        usuario = procurar_usuario_no_banco(email)
    except EmailInvalido as e:
        print(f'Informar usuária para corrigir email. Razão do erro: {e.msg_de_erro}')
    except UsuarioNaoEncontrado as e:
        print('Usuário não encontrado')
    except Exception:
        pass
    else:
        print(f'Enviando email para: {email}')
        print(f'Mensagem para {usuario}')
    finally:
        pass


if __name__ == '__main__':
    enviar_email_de_boas_vindas('renzo@python.pro.br')
    enviar_email_de_boas_vindas('river')
    enviar_email_de_boas_vindas('river@python.pro.br')
