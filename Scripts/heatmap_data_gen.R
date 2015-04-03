library(diversitree)
args <- commandArgs(TRUE)
args <- commandArgs(trailingOnly = TRUE)
data <- read.csv('./Data/PyronParityData.csv', row.names=1)
a_vec <- seq(0.1,1,.1)
b_vec <- seq(0.1,1,.1)
outvec <- vector()
x <- (args[1])
phy <- read.tree(x)
print(phy)
phy <- multi2di(phy, random = TRUE)
pruned.tree<-drop.tip(phy, setdiff(phy$tip.label, row.names(data)))
sorteddata <- data[phy$tip.label, ]
no_na <- na.omit(sorteddata)
names(no_na) <- pruned.tree$tip.label
for (x in a_vec){
    for (y in b_vec){
        func2 <- make.bisse(pruned.tree,no_na, sampling.f = c(x, y))
	    sp<-starting.point.bisse(pruned.tree)
        fit_bisse <- find.mle(func2, sp)
        st2 <- asr.marginal(func2, coef(fit_bisse))
        rootst <- st2[1,1]
        outvec <- append(outvec, rootst)
        print(outvec)
        }
    }
txt <- paste(args, '_data.csv', sep = '')
write.table(outvec, file=txt)


