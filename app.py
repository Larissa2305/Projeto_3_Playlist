import streamlit as st

generos = {
    'Kpop': {
        'Aespa': 'https://www.youtube.com/watch?v=WPdWvnAAurg',
        'Stray Kids': 'https://www.youtube.com/watch?v=P7vBoGWoReg',
        'Katseye': 'https://www.youtube.com/watch?v=R2-yomhYAj4',
        'Enhypen': 'https://www.youtube.com/watch?v=rDolt3jJRsM',
    },
    'Internacional': {
        'Tyla': 'https://www.youtube.com/watch?v=SZpiiixlHWY',
        'Chase Atlantic': 'https://www.youtube.com/watch?v=4kbSC3HXfJw',
        'Beyoncé': 'https://www.youtube.com/watch?v=rNM5HW13_O8',
        'Justin Bieber': 'https://www.youtube.com/watch?v=kffacxfA7G4', 
    },
    'Rap': {
        'Eminem': 'https://www.youtube.com/watch?v=8kYkciD9VjU',
        'Nicki Minaj': 'https://www.youtube.com/watch?v=0HDdjwpPM3Y',
        'Jay-z': 'https://www.youtube.com/watch?v=vk6014HuxcE',
        'Hungria': 'https://www.youtube.com/watch?v=EiQmbrvvDaY',
    },
    'Pop Brasileiro': {
        'IZA': 'https://www.youtube.com/watch?v=FnGfgb_YNE8',
        'Marina Sena': 'https://www.youtube.com/watch?v=0vEPVBtkyaU',
        'Jão': 'https://www.youtube.com/watch?v=zeqcOvSMddU',
        'Luiz Gonzaga': 'https://www.youtube.com/watch?v=zsFSHg2hxbc',
    }
}

#-------------------------------------------------------------------Sidebar

st.sidebar.title('lively music')
st.sidebar.image('logo.png')

genero = st.sidebar.selectbox('Escolha um genero musical',generos.keys())

artista = st.sidebar.selectbox('Escolha um artista', generos[genero])


#--------------------------------------------------------------------Body

st.title(artista)
st.markdown('---')
video, sobre = st.tabs(['Vídeo', 'Sobre o artista'])

with video:
    st.video(generos[genero][artista])

with sobre:
    if artista == 'Aespa':
        st.markdown("""
                    Aespa (hangul: 에스파; rr: eseupa; MR: esŭp'a, comumente estilizado em letras minúsculas ou æspa) é um girl group sul-coreano formado pela SM Entertainment. O grupo é composto por quatro integrantes: Karina, Winter, Giselle e Ningning. O grupo é conhecido por popularizar o conceito de metaverso e o gênero hyperpop no K-pop.[1][2][3]

                    Aespa estreou em 17 de novembro de 2020, com o single "Black Mamba", que alcançou o maior número de visualizações em 24 horas para o vídeo de estreia de um grupo de K-pop. Seu segundo single, "Next Level", foi lançado em maio de 2021 com amplo sucesso comercial e de crítica, alcançando a segunda posição no Circle Digital Chart e ganhando o prêmio Daesang[a] para Canção do Ano no 19º Korean Music Awards. Em outubro do mesmo ano, Aespa lançou seu primeiro extended play (EP) Savage e seu single de mesmo nome. O EP se tornou o álbum de estreia de maior sucesso de um girl group de K-pop na parada americana Billboard 200 na posição 20, enquanto o último atingiu o pico na posição dois na Coreia do Sul e marcou sua primeira entrada no top 40 na Billboard Global 200.

                    """)
        
    elif artista == 'Stray Kids':
        st.markdown("""
                    Stray Kids (em coreano: 스트레이 키즈; romaniz.: Seuteurei kijeu; comumente abreviado como SKZ) é um grupo masculino sul-coreano formado pela JYP Entertainment. É composto por oito integrantes: Bang Chan, Lee Know, Changbin, Hyunjin, Han, Felix, Seungmin e I.N. Por motivos pessoais não revelados, Woojin deixou o grupo em outubro de 2019. Stray Kids produz suas próprias gravações; a equipe principal de produção se chama 3Racha e consiste em Bang Chan, Changbin e Han, e os outros membros frequentemente participam da composição das músicas.

                    Bang Chan selecionou cada membro para fazer parte do grupo antes das filmagens do reality show homônimo de 2017, o que é incomum no K-pop, onde esse poder normalmente recai sobre executivos e diretores criativos.[1] O grupo lançou seu primeiro extended play (EP) de estreia não oficial, Mixtape, em janeiro de 2018, e estreou oficialmente em 25 de março com o EP I Am Not, seguido pelos EPs I Am Who e I Am You, completando a série I Am.[2] A trilogia Clé, composta por Clé 1: Miroh, Clé 2: Yellow Wood e Clé: Levanter, foi lançada em 2019.

                    """)

    elif artista == 'Katseye':
        st.markdown("""
                    Katseye (em inglês: Katseye; estilizado em letras maiúsculas; referência à gema e traduzido para o português como Olho de Gato) é um grupo feminino formado pela Hybe UMG e Geffen Records e baseado em Los Angeles. O grupo é composto por seis integrantes: Manon, Sophia, Daniela, Lara, Megan e Yoonchae. Com membros da Filipinas, Coreia do Sul, Suíça e Estados Unidos (com raízes ligadas diretamente a Venezuela, Cuba, Índia, Suécia, Singapura e China)[1][2][3], é comumente descrito como um grupo feminino global.[4][5]

                    O grupo foi formado por meio do reality show de competição Dream Academy, em 2023, em uma colaboração entre a Hybe UMG e a Geffen Records. O processo de formação do grupo foi posteriormente documentado na série da Netflix, Popstar Academy: Katseye, que narrou as audições, o treinamento intenso, e a formação do grupo. Katseye debutou em 28 de junho de 2024 com o single Debut[6], seguido do seu single de sucesso Touch, lançado em 5 de agosto de 2024. Mais tarde, elas lançaram o seu primeiro extended play (EP), SIS (Soft is Strong) em 16 de agosto de 2024. Em 30 de abril de 2025, o grupo lançou Gnarly que, apesar de receber reações mistas no dia de lançamento, atraiu atenção significativa e rendeu ao grupo sua primeira entrada na Billboard Hot 100; acompanhado do single Gabriela, lançado em 20 de junho de 2025. O segundo extended play (EP), Beautiful Chaos, foi lançado em 27 de junho de 2025, estreando no número 4 da Billboard 200, seu lançamento com a maior posição até o momento.


                    """)    
    
    elif artista == 'Enhypen':
        st.markdown("""
                    Em março de 2019, o Belift Lab foi cofundado pelas agências de entretenimento sul-coreanas CJ E&M e Hybe Corporation , com planos de criar uma nova banda em 2020. [ 8 ] As audições começaram no mesmo mês em Seul, Estados Unidos, Taiwan e Japão, entre outros locais, buscando trainees do sexo masculino nascidos entre 1997 e 2008. [ 9 ] [ 10 ] [ 11 ]

                    Em 8 de maio de 2020, o canal de televisão Mnet anunciou a série de competição de sobrevivência I-Land como parte da joint venture entre as duas empresas de entretenimento que "segue o processo de nascimento dos artistas de K-pop da próxima geração". [ 11 ] [ 12 ] [ 13 ] O Enhypen foi formado por meio do programa, que contou com 23 trainees do sexo masculino, alguns dos quais foram originalmente testados para o Belift, enquanto outros foram transferidos da Big Hit Music . O programa foi ao ar semanalmente na Mnet de 26 de junho a 18 de setembro de 2020 e internacionalmente no canal do YouTube da Hybe Labels . [ 14 ] [ 15 ] [ 16 ] A série foi dividida em duas partes, com os 12 melhores competidores da primeira parte avançando para a segunda. [ 14 ] No último episódio do programa, sete membros foram selecionados entre os nove competidores finais, com seis escolhidos por classificações globais e um por escolha dos produtores. [ 17 ] [ 18 ] A escalação final de Heeseung, Jay, Jake, Sunghoon , Sunoo, Jungwon e Ni-Ki foi anunciada na transmissão ao vivo da final. 


                    """)   

    elif artista == 'Tyla':
        st.markdown("""
                    Tyla Laura Seethal (Joanesburgo, 30 de janeiro de 2002), conhecida mononimamente como Tyla, é uma cantora e compositora sul-africana. Assinou contrato com a Epic Records em 2021 após o sucesso nacional de seu single de estreia "Getting Late", com Kooldrink. Tyla ganhou destaque internacional com seu single "Water", de 2023, que entrou nas paradas em dezessete países, inclusive alcançando o top dez do UK Singles Chart. Isso também fez dela a primeira solista sul-africana em 55 anos a entrar na Billboard Hot 100 dos Estados Unidos. Seu estilo musical é caracterizado por uma fusão de pop e amapiano, com muitas publicações a apelidando de "Rainha do Popiano".

                    """) 

    elif artista == 'Chase Atlantic':
        st.markdown("""
                    Chase Atlantic (estilizado em letras maiúsculas ) é uma banda australiana de R&B de Cairns , Queensland , formada em 2014. A banda é composta por três integrantes: Christian Anthony e os irmãos Mitchel e Clinton Cave, e lançou sete EPs e quatro álbuns desde sua formação. Eles são mais conhecidos pelo single de sucesso de 2017, "Swim".
                    
                    """)   
        
    elif artista == 'Beyoncé':
        st.markdown("""
                    Beyoncé Giselle Knowles-Carter nascida em 4 de setembro de 1981) é uma cantora, compositora, atriz e empresária americana. Conhecida por sua habilidade vocal, reinvenções artísticas eapresentações ao vivo, ela é amplamente consideradauma das figuras culturalmente mais significativas do século XXI. Creditada por moldara música popular, Beyoncé é frequentemente considerada uma das maiores artistas e artistas mais influentes de todos os tempos. [ 4 ]

                    Beyoncé alcançou a fama em 1997 como vocalista principal do Destiny's Child , um dos grupos femininos mais vendidos de todos os tempos . Seu álbum solo de estreia, Dangerously in Love (2003), tornou-se um dos álbuns mais vendidos do século XXI . Após a dissolução do Destiny's Child em 2005, Beyoncé lançou o funk B'Day ( 2006 ) e estrelou o filme dramático Dreamgirls (2006). Seu casamento com o rapper Jay-Z e a interpretação de Etta James no filme biográfico Cadillac Records (2008) influenciaram seu álbum duplo de orientação pop I Am... Sasha Fierce (2008). Ao longo dos anos 2000, Beyoncé conquistou os singles número um da Billboard Hot 100 dos EUA " Crazy in Love ", " Baby Boy ", " Irreplaceable ", " Check on It " e " Single Ladies (Put a Ring on It) ".

                    """)  

    elif artista ==  'Justin Bieber':
        st.markdown("""
                    Justin Drew Bieber ( / ˈ b iː b ər / BEE -bər ; nascido em 1 de março de 1994) [ 1 ] [ 2 ] é um cantor e compositor canadense. Considerado um ícone pop , ele é conhecido por suas performances musicais multigênero. [ 3 ] [ 4 ] Ele foi descoberto por Scooter Braun em 2008 e trazido para os EUA por Usher , ambos formaram a RBMG Records para assinar com Bieber em outubro daquele ano. Seu primeiro extended play , My World (2009), foi recebido com reconhecimento internacional e o estabeleceu como um ídolo adolescente .

                    Bieber alcançou a fama mainstream com seu álbum de estreia, My World 2.0 (2010), que liderou a Billboard 200 dos EUA — tornando-o o mais jovem artista solo masculino a fazê-lo em 47 anos. [ 5 ] Seu primeiro single, " Baby " (com Ludacris ), tornou-se um dos singles mais vendidos nos EUA. [ 6 ] Seu segundo álbum, Under the Mistletoe (2011), tornou-se o primeiro álbum de Natal de um artista masculino a estrear no topo das paradas. [ 7 ] Bieber explorou o dance-pop em seu terceiro álbum, Believe (2012); seu relançamento acústico fez dele o primeiro artista na história da Billboard a ter cinco álbuns número um nos EUA aos 18 anos. [ 8 ]

                    """)    

    elif artista ==  'Eminem':
        st.markdown("""
                    Marshall Bruce Mathers III (nascido em 17 de outubro de 1972), conhecido profissionalmente como Eminem , [ a ] é um rapper, compositor e produtor musical americano. Considerado um dos maiores e mais influentes rappers de todos os tempos, ele é creditado por popularizar o hip-hop na América Central e quebrar barreiras raciais para a aceitação de rappers brancos na música popular. Embora grande parte de seu trabalho transgressivo durante o final dos anos 1990 e início dos anos 2000 o tenha tornado uma figura controversa , Eminem se tornou uma representação da angústia popular da subclasse americana e é conhecido por suas letras conscientes , com críticas políticas e comentários sociais , e um fluxo de rap habilidoso .

                    Após o lançamento de seu álbum de estreia Infinite (1996) e do EP Slim Shady ( 1997), Eminem assinou com a Aftermath Entertainment do Dr. Dre e posteriormente alcançou popularidade em 1999 com The Slim Shady LP . Seus dois lançamentos seguintes, The Marshall Mathers LP (2000) e The Eminem Show (2002), tornaram-se sucessos mundiais. Cada um vendeu mais de um milhão de cópias em uma única semana , sendo este último o álbum mais vendido no mundo em 2002 e o álbum de hip-hop mais vendido de todos os tempos . Após o lançamento de Encore (2004), Eminem fez uma pausa devido, em parte, às lutas contra o vício em medicamentos prescritos. Mais tarde, ele retornou à indústria musical com os lançamentos de Relapse (2009) e Recovery (2010), este último se tornando o álbum mais vendido no mundo em 2010. Cada um de seus lançamentos subsequentes — The Marshall Mathers LP 2 (2013), Revival (2017), Kamikaze (2018), Music to Be Murdered By (2020) e The Death of Slim Shady (Coup de Grâce) (2024) — estreou no topo da parada Billboard 200 .

                    """)   

    elif artista ==  'Nicki Minaj':
        st.markdown("""
                    Onika Tanya Maraj (Saint James, 8 de dezembro de 1982), conhecida por seu nome artístico Nicki Minaj, é uma rapper, cantora, compositora, modelo e atriz trinidiana radicada nos Estados Unidos.[5] Minaj nasceu no país caribenho e mudou-se para o bairro nova-iorquino do Queens quando tinha cinco anos de idade, se formando em escolas artísticas mais tarde. Depois de lançar três mixtapes entre 2007 e 2009, assinou um contrato com a gravadora Young Money.

                    Ela lançou seu álbum de estreia, Pink Friday (2010) e atingiu o topo da tabela estado-unidense de discos mais vendidos Billboard 200 e certificado de disco de platina pela Recording Industry Association of America (RIAA) após um mês da sua distribuição.[6][7] A canção "Super Bass" foi certificada em platina quádrupla pela RIAA, e já vendeu mais de oito milhões de cópias digitais, tornando-se um dos singles mais vendidos nos Estados Unidos.[8] Minaj se tornou a primeira artista a ter sete canções como singles na lista de músicas Billboard Hot 100 ao mesmo tempo.

                    """)    

    elif artista == 'Jay-z':
        st.markdown("""
                    Shawn Corey Carter (Nova Iorque, 4 de dezembro de 1969), mais conhecido pelo seu nome artístico JAY-Z, é um rapper, compositor, produtor musical e empresário norte-americano. Enraizado no hip hop da Costa Leste, ele foi nomeado o melhor rapper de todos os tempos pela Billboard e pela Vibe em 2023.[4] Ele atuou como presidente e diretor executivo da Def Jam Recordings de 2004 a 2007 e fundou a empresa de entretenimento Roc Nation no ano seguinte.[5]

                    Protegido do rapper Jaz-O, de Nova Iorque, Jay-Z começou sua carreira musical no final da década de 1980; ele foi cofundador da gravadora Roc-A-Fella Records em 1994 para lançar seus dois primeiros álbuns de estúdio, Reasonable Doubt (1996) e In My Lifetime, Vol. 1 (1997), ambos recebidos com aclamação da crítica. Todos os seus onze álbuns seguintes, incluindo The Blueprint (2001), The Black Album (2003), American Gangster (2007) e 4:44 (2017), estrearam no topo da Billboard 200; Jay-Z detém o recorde conjunto de solista com a maior quantidade de álbuns (14) que lideraram o gráfico (empatado com Drake e Taylor Swift).[6][7][8][9] Ele também lançou os álbuns colaborativos The Best of Both Worlds (2002) e Unfinished Business (2004) com o cantor R. Kelly,[10] Collision Course (2004) com Linkin Park, Watch the Throne (2011) com Kanye West e Everything Is Love (2018) com sua esposa Beyoncé.[11] Ele alcançou o topo da Billboard Hot 100 em quatro ocasiões: uma vez como artista principal com "Empire State of Mind" (com participação de Alicia Keys) e três vezes como convidado especial com as canções "Heartbreaker" de Mariah Carey, "Crazy in Love" de Beyoncé e "Umbrella" de Rihanna.

                    """)   

    elif artista ==  'Hungria':
        st.markdown("""
                    A Hungria (em húngaro: Magyarország, pronunciado:  é um país localizado na Europa Central, especificamente na Bacia dos Cárpatos. Faz fronteira com a Eslováquia ao norte, Romênia ao leste, Sérvia ao sul, Croácia a sudoeste, Eslovênia a oeste, Áustria a noroeste e Ucrânia a nordeste. A capital do país é a cidade de Budapeste. A Hungria é membro da União Europeia, da OTAN, da OCDE, do Grupo de Visegrád e do Espaço Schengen. A língua oficial é o húngaro, que é a língua não indo-europeia mais falada na Europa.[9]

                    Após séculos de sucessiva ocupação de celtas, romanos, hunos, eslavos, gépidas e ávaros, a Hungria foi fundada no final do século IX pelo grão-príncipe húngaro Arpades durante o Honfoglalás ("conquista da pátria"). Seu bisneto Estêvão I subiu ao trono no ano 1000, quando converteu o país para um reino cristão. Até o século XII, a Hungria era uma potência média no mundo ocidental, alcançando seu auge no século XV.[10] Após a Batalha de Mohács, em 1526, e de cerca de 150 anos sob ocupação otomana (1541-1699), a Hungria ressurge sob o domínio dos Habsburgos e, mais tarde, formou uma parte significativa do Império Austro-Húngaro (1867-1918).
                    """)    

    elif artista == 'IZA':
        st.markdown("""
                    Isabela Cristina Correia de Lima Lima (Rio de Janeiro, 3 de setembro de 1990), mais conhecida como IZA (também estilizado como Iza), é uma cantora e compositora brasileira. Com uma voz potente e credibilidade artística, é um dos maiores nomes da música pop e R&B nacional.

                    Seu primeiro álbum, Dona de Mim, foi lançado em 2018 e recebeu uma indicação ao Grammy Latino de Melhor Álbum Pop Contemporâneo em Língua Portuguesa. Iza já conta com quatro indicações ao Grammy Latino. [4][5] Em 2019, Iza estreou como jurada no The Voice Brasil, onde permanceu até 2023 e foi anunciada como rainha de bateria da Imperatriz Leopoldinense.

                    """)     

    elif artista ==  'Marina Sena':
        st.markdown("""
                    Marina de Oliveira Sena (Taiobeiras, 26 de setembro de 1996), conhecida como Marina Sena, é uma cantora e compositora brasileira do norte de Minas Gerais. Iniciou sua carreira como vocalista do grupo montes-clarense A Outra Banda da Lua, com apresentações em várias cidades do estado. Ganhou destaque nacional com a banda belo-horizontina Rosa Neon.

                    Em 2021, Sena lançou sua carreira solo com o álbum De Primeira, que a consolidou como um nome promissor na música pop brasileira. O trabalho rendeu três troféus no Prêmio Multishow de Música Brasileira e duas indicações ao Grammy Latino. Após assinar com a Sony Music Brasil, lançou Vício Inerente, seu segundo álbum, que trouxe um som mais comercial e radiofônico. Seu terceiro disco, Coisas Naturais, apresentou maior diversidade musical, resgatando as raízes de sua época com A Outra Banda da Lua e alcançando o top 10 das maiores estreias mundiais da semana no Spotify.
                    """)       
        
    elif artista == 'Jão':
        st.markdown("""
                    João Vitor Romania Balbino (Américo Brasiliense, 3 de novembro de 1994), mais conhecido como Jão, é um cantor e compositor brasileiro. Ele começou sua carreira musical em 2016, postando covers de canções no aplicativo de compartilhamento de vídeos YouTube. Ele chamou a atenção dos produtores Pedro Dash e Marcelinho Ferraz, o que o levou a assinar um contrato com a Head Media, selo da Universal Music Group. Ele lançou seu single de estreia, "Dança pra Mim" (com Pedrowl), em novembro de 2016. O extended play (EP) de estreia de Jão intitulado Primeiro Acústico foi lançado em junho de 2018, seguido por seu primeiro álbum de estúdio, Lobos, em agosto do mesmo ano.

                    A descoberta de Jão veio quando seu single "Imaturo" recebeu um reconhecimento significativo. Seu segundo álbum de estúdio, Anti-Herói, foi lançado em outubro de 2019, e foi apoiado pelos singles "Enquanto Me Beija" e "Essa Eu Fiz pro Nosso Amor". O álbum estreou todas as suas 10 faixas no top 200 do Spotify Brasil. Seu terceiro álbum de estúdio, Pirata, foi lançado em outubro de 2021. O single "Idiota" foi a canção do álbum que mais se destacou, alcançando a segunda posição nas rádios pop do Brasil e o top 20 na parada de singles de Portugal. No Grammy Latino de 2022, Pirata foi indicado para Melhor Álbum Pop Contemporâneo em Língua Portuguesa, enquanto "Idiota" foi indicada para Melhor Canção em Língua Portuguesa. Ele lançou seu quarto álbum, Super, em 14 de agosto de 2023.

                    """)    
        
    elif artista == 'Luiz Gonzaga':
        st.markdown("""
                    Luiz Gonzaga do Nascimento (Exu, 13 de dezembro de 1912 Recife, 2 de agosto de 1989) foi um cantor, compositor e multi-instrumentista brasileiro. Também conhecido como o Rei do Baião, foi considerado uma das mais completas, importantes e criativas figuras da música popular brasileira.[4]

                    Cantando acompanhado de sua sanfona, zabumba e triângulo (conjunto básico dos cantores de baião, que ele mesmo definiu), levou para todo o país a cultura musical do nordeste, como o baião, o xaxado, o xote e o forró pé de serra. Suas composições também descreviam a pobreza, as tristezas e as injustiças de sua árida terra, o sertão nordestino. Era torcedor declarado do Santa Cruz Futebol Clube.[6]

                    Luiz Gonzaga ganhou notoriedade com as antológicas canções "Asa Branca" (1947), "Juazeiro" (1948) e "Baião de Dois" (1950).

                    Pai adotivo do músico Gonzaguinha, Gonzagão influenciou outros artistas da MPB como Geraldo Vandré, Raul Seixas, Gilberto Gil e Caetano Veloso.

                    """)    




