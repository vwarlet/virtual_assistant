def format_hour(hour):
    if hour == '00':
        hour = 'meia noite'
    if hour == '01':
        hour = 'uma'
    if hour == '02':
        hour = 'duas'
    if hour == '03':
        hour = 'três'
    if hour == '04':
        hour = 'quatro'
    if hour == '05':
        hour = 'cinto'
    if hour == '06':
        hour = 'seis'
    if hour == '07':
        hour = 'sete'
    if hour == '08':
        hour = 'oito'
    if hour == '09':
        hour = 'nove'
    if hour == '10':
        hour = 'dez'
    if hour == '11':
        hour = 'onze'
    if hour == '12':
        hour = 'meio dia'
    if hour == '13':
        hour = 'uma'
    if hour == '14':
        hour = 'duas'
    if hour == '15':
        hour = 'três'
    if hour == '16':
        hour = 'quatro'
    if hour == '17':
        hour = 'cinco'
    if hour == '18':
        hour = 'seis'
    if hour == '19':
        hour = 'sete'
    if hour == '20':
        hour = 'oito'
    if hour == '21':
        hour = 'nove'
    if hour == '22':
        hour = 'dez'
    if hour == '23':
        hour = 'onze'
    return hour

def format_minutes(minutes):
    if minutes == '00':
        minutes = 'em ponto'
    if minutes == '01':
        minutes = 'um'
    if minutes == '02':
        minutes = 'dois'
    if minutes == '03':
        minutes = 'três'
    if minutes == '04':
        minutes = 'quatro'
    if minutes == '05':
        minutes = 'cinto'
    if minutes == '06':
        minutes = 'seis'
    if minutes == '07':
        minutes = 'sete'
    if minutes == '08':
        minutes = 'oito'
    if minutes == '09':
        minutes = 'nove'
    return minutes

def curiosities():
    curious = [
        'Existem mais galinhas do que pessoas no mundo.',
        'As máquinas de venda automática matam 4 vezes mais pessoas do que tubarões por ano.',
        'O microondas foi inventado depois que um pesquisador passou por um tubo de radar e uma barra de chocolate derreteu em seu bolso.',
        'Fredric Baur inventou a lata de PringlQuando ele faleceu em 2008, suas cinzas foram enterradas em uma.',
        'Historicamente, mais ligações a cobrar são feitas no Dia dos Pais do que em qualquer outro dia do ano.',
        'A psicologia é o cérebro tentando compreender a si mesmo.',
        'Se você gritar initerruptamente por 8 anos, 7 meses e cinco dias, terá produzido energia sonora suficiente para aquecer uma xícara de café.',
        'Em média, uma criança de quatro anos faz mais de quatrocentas perguntas por dia.',
        'As mulheres piscam quase duas vezes mais que os homens.',
        'Os humanos perdem 18 quilos de pele ao longo da vida, substituindo completamente a pele externa a cada mês.',
        'Os selos oferecem cerca de um décimo de caloria quando você os lambe.',
        'O medo de barbas existe! Aliás, é chamado de pogonofobia.',
        'O ser humano adulto médio tem de um a quatro quilos de bactérias em seu corpo.',
        'O peso total de todas as formigas na Terra é maior do que o peso total de todos os humanos no planeta.',
    ] 
    return curious