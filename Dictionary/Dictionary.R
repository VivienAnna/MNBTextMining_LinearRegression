install.packages("installr")
installr::install.Rtools()
install.packages("devtools")
devtools::install_github("poltextlab/HunMiner")
library(HunMiner)
poltext_szotar <- HunMineR::dictionary_poltext
