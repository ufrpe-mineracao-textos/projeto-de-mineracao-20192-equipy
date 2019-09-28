import twint

c = twint.Config()

c.Search = "depressão"   #Depressão, ansiedade, etc...
c.Limit = 300
c.Store_csv = True
c.Lang = "pt"
c.Output = "resultados"

twint.run.Search(c)