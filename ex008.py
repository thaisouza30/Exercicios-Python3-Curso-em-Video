medida = float(input('Uma distância em metros:'))
dm = medida * 10
cm = medida * 100
mm = medida * 1000
km = medida / 1000
hm = medida / 100
dam = medida / 10
print('A medida de {}m corresponde a {}dm '.format(medida,dm))
print('A medida de {}m corresponde a {}cm'.format(medida,cm))
print('A medida de {}m corresponde a {}mm'.format(medida,mm))
print('A medida de {}m corresponde a {}km'.format(medida,km))
print('A medida de {}m corresponde a {}hm'.format(medida,hm))
print('A medida de {}m corresponde a {}dam'.format(medida,dam))

