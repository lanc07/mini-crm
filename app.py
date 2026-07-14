from models import Lead
from stages import DEFAULT_STAGE
from repo import LeadRepository

lead_backend = LeadRepository()

def add_lead():
    print("Add lead")
    name = input('nome: ')
    company = input('empresa: ')
    email = input('email: ')

    lead = Lead(name, company, email, DEFAULT_STAGE)
    modeled_lead = lead.model_lead()
    lead_backend.create_lead(modeled_lead)
    print('lead adicionado')

def search_leads():
    search = input("Buscar por: "). strip().lower()

    if not search:
        print("Consulta vazia")
        return

    leads = lead_backend.read_leads()
    results = []

    for i, lead in enumerate(leads):
        lead_str = f'{lead['name']} {lead['company']} {lead['email']}'.lower()
        if search in lead_str:
            results.append(lead)

    if not results:
        print("nada encontrado")
        return

    print(f"\n# | {'Nome: <20'} | {"Empresa: <20"} | {"E-mail: <20"}")

    for i, lead in enumerate(results):
        print(f'{i:02d} | {lead["name"]: <20} | {lead["company"]: <20} | '
              f'{lead['email']: <20}')


def export_leads():
    path_csv = lead_backend.export_csv()

    if path_csv is None:
        print('Não foi possível exportar o CSV... Feche o arquivo e tente '
              'novamente')
    else:
        print(f'CSV exportado para: {path_csv}')

def list_lead():
    leads = lead_backend.read_leads()
    if not leads:
         print("nenhum lead ainda")
         return

    print(  f"\n# | {'Nome: <20'} | {"Empresa: <20"} | {"E-mail: <20"}")

    for i, lead in enumerate(leads):
        print(f'{i:02d} | {lead["name"]: <20} | {lead["company"]: <20} | '
              f'{lead['email']: <20}')

def main():
    while True:
        print_menu()
        op = input('Escolha: ')

        if op == '1':
            print(add_lead())
        elif op == '2':
            print(list_lead())

        elif op == '3':
            search_leads()
        elif op == '4':
            export_leads()
        elif op == '5':
            print('Saindo')
        else:
            print('opção inválida')

def print_menu():
    print('menu CRM de leads ')
    print("[1] adicionar lead")
    print('[2] listar leads')
    print('[3] Buscar leads')
    print('[4] Exportar CSV')
    print('[5] Sair')

if __name__ == "__main__":
    main()

