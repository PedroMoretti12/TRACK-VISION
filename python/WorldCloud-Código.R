install.packages("tidyverse")
install.packages("tm")
install.packages("wordcloud")
install.packages("wordcloud2")
install.packages("RColorBrewer")
library(tm)
library(wordcloud,wordcloud2)
library(RColorBrewer)
problemas = c(rep("ram_elevada",4),rep("processos_altos",5),rep( "serviços_elevados",2),rep("cpu_vazia",4), rep("energia_alta",5), rep("temperatura_acima",3),rep("memoria_ultrapassando",2),rep("angulatura_alta",4),rep("custo_alto",2),rep("dashboard_travando",3))
problemas20x = rep(c(problemas),20)
amostra1 = sample(problemas20x,300,replace =TRUE)
docs1<-Corpus(VectorSource(amostra1))
dtm<-TermDocumentMatrix(docs1)
dtm
matrizdocs1<-as.matrix(dtm)
words<-sort(rowSums(matrizdocs1),decreasing=TRUE)
df<-data.frame(word=names(words),freq=words)
df1=df[df$freq>1.0,]
View(df1)
wordcloud(words=df1$word, freq=df$freq, min.freq = 2,max.words = 100,random.order = FALSE,,colors = brewer.pal(8,"Dark2"))

 