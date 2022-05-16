# Regra: A figura deve ter os canais RBG, (X, Y, 3). Algumas figuras, na conversão da linha 9,
# ficam com valores abaixo de 1 em todos os píxels, caso isso aconteça cada ponto deve
# ser multiplicado por 100

import pylab
import matplotlib.pyplot as plt
import numpy as np
img = pylab.imread("img2.jpg")
img_gray = 0.299 * img[:,:,0] + 0.587 * img[:,:,1] + 0.114 * img[:,:,2]


##Função de subamostragem##
#Essa função recebe a imagem e a escala decimal de amostragem a qual a imagem  será convertida,
#ela elimina as linhas e colunas intercaladamente. O processo é repetido até que a escala seja
#alcançada. Cada loop principal reduz a qualidade da figura em 50%
def Reduzir_Dim(reducao,imagem):
    escala = int(1/reducao)
    Imagem = imagem
    for k in range(int(escala/2)):
        for i in range(int(len(Imagem)/2)):
            Imagem = np.delete(Imagem,obj=i, axis=0)
        for j in range(int(np.size(Imagem,1)/2)):
            Imagem = np.delete(Imagem,obj=j, axis=1)
    return Imagem

#Aplicando a função com diferentes valores de amostragem#
imgs1 = Reduzir_Dim(0.5,img_gray)
print(imgs1.shape)
imgs2 = Reduzir_Dim(0.25,img_gray)
print(imgs2.shape)
imgs3 = Reduzir_Dim(0.125,img_gray)
print(imgs3.shape)


#plota as imagens#
f, axarr = plt.subplots(2,3)
axarr[0,1].imshow(img_gray,pylab.cm.gray)
axarr[0,1].set_title('Imagem original')
axarr[1,0].imshow(imgs1,pylab.cm.gray)
axarr[1,0].set_title('50% de amostragem')
axarr[1,1].imshow(imgs2,pylab.cm.gray)
axarr[1,1].set_title('25% de amostragem')
axarr[1,2].imshow(imgs3,pylab.cm.gray)
axarr[1,2].set_title('12,5% de amostragem')
f.delaxes(axarr[0,0])
f.delaxes(axarr[0,2])
f.suptitle('Redução de amostragem')
plt.show()

