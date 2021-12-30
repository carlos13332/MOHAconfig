from tkinter import *

root = Tk()
root.title('Arquivo de config - MOHA')
root.minsize(320,380)
root.maxsize(320,380)
root.geometry('320x380')

var = IntVar()
var2 = IntVar()
var3 = IntVar()
screen = ''
configfile = ''
w = 0
h = 0
#resolução
def treso():
    global w
    global h
    op = var3.get()
    if op == 1:
        w = 800
        h = 600
    elif op == 2:
        w = 1024
        h = 768
    elif op == 3:
        w = 1280
        h = 720
    elif op == 4:
        w = 1360
        h = 768
    elif op == 5:
        w = 1366
        h = 768
    elif op == 6:
        w = 1920
        h = 1080
        
text1 = Label(root, text='Selecione uma resolução:')
text1.pack()        
Reso1 = Radiobutton(root, text='800x600', variable=var3, value=1,command=treso)
Reso1.pack( anchor = W )
Reso2 = Radiobutton(root, text='1024x768', variable=var3, value=2,command=treso)
Reso2.pack( anchor = W )
Reso3 = Radiobutton(root, text='1280x720', variable=var3, value=3,command=treso)
Reso3.pack( anchor = W )
Reso4 = Radiobutton(root, text='1360x768', variable=var3, value=4,command=treso)
Reso4.pack( anchor = W )
Reso5 = Radiobutton(root, text='1366x768', variable=var3, value=5,command=treso)
Reso5.pack( anchor = W )
Reso6 = Radiobutton(root, text='1920x1080', variable=var3, value=6,command=treso)
Reso6.pack( anchor = W )
#modo janela ou tela cheia
texto = Label(root, text='Selecione tela cheia ou modo janela:')
texto.pack()
def ftela():
    global screen
    screen = 'True'
def jtela():
    global screen
    screen = 'False'
R1 = Radiobutton(root, text='Tela Cheia', variable=var, value=1,command=ftela)
R1.pack( anchor = W )
R2 = Radiobutton(root, text='Modo Janela', variable=var, value=2,command=jtela)
R2.pack( anchor = W )

#baixo, medio ou alto
texto2 = Label(root, text='Selecione os graficos:')
texto2.pack()
def lowg():
    global screen
    global configfile
    global w
    global h
    configfile = '''
[ALAudio.ALAudioDevice]
MaxChannels=20
UseEffectsProcessing=False

[MOHAGame.MOHAScalabilityOptions]
bTickLODAnims=True
bAllowDynamicDecals=True
bAllowDynamicLights=True
bAllowDynamicShadows=True
bAllowLightEnvironmentShadows=True
bAllowStaticDecals=False
MaxNumberOfDynamicDecals=20
MaxNumberOfStaticDecals=0
MaxParticlesAllowed=500
ParticleCullExemptDistance = 4000
ParticleLODBias=3

[TextureLODSettings]
TEXTUREGROUP_Character=(MinLODSize=64,MaxLODSize=1024,LODBias=2)
TEXTUREGROUP_CharacterNormalMap=(MinLODSize=64,MaxLODSize=1024,LODBias=2)
TEXTUREGROUP_Effects=(MinLODSize=64,MaxLODSize=1024,LODBias=2)
TEXTUREGROUP_LightAndShadowMap=(MinLODSize64,MaxLODSize=1024,LODBias=2)
TEXTUREGROUP_RenderTarget=(MinLODSize=1,MaxLODSize=1024,LODBias=2)
TEXTUREGROUP_Skybox=(MinLODSize=64,MaxLODSize=1024,LODBias=2)
TEXTUREGROUP_UI=(MinLODSize=256,MaxLODSize=4096,LODBias=0)
TEXTUREGROUP_Vehicle=(MinLODSize=64,MaxLODSize=1024,LODBias=2)
TEXTUREGROUP_VehicleNormalMap=(MinLODSize=64,MaxLODSize=1024,LODBias=2)
TEXTUREGROUP_Weapon=(MinLODSize=64,MaxLODSize=1024,LODBias=2)
TEXTUREGROUP_WeaponNormalMap=(MinLODSize=64,MaxLODSize=1024,LODBias=2)
TEXTUREGROUP_World=(MinLODSize=64,MaxLODSize=1024,LODBias=2)
TEXTUREGROUP_WorldNormalMap=(MinLODSize=64,MaxLODSize=1024,LODBias=2)

[WinDrv.WindowsClient]
StartupResolutionX=%s
StartupResolutionY=%s
StartupFullscreen=%s

[MOHAGame.MOHAScalabilityOptions]
bGroupShadows=True
bForceFallbackShader=True
bAllowBloom=False
bAllowDepthOfField=False
bAllowMotionBlur=False
bPostFX=False
bSimplePostFX=False
ScreenPercentage=100.0
bMinspecCull=True
SkeletalMeshLODBias=1
StaticMeshLODBias=2
CullDistanceBiasBase=0.4
''' % (w,h,screen)
def medg():
    global screen
    global configfile
    global w
    global h
    configfile ='''
[ALAudio.ALAudioDevice]
MaxChannels=90
UseEffectsProcessing=False

[MOHAGame.MOHAScalabilityOptions]
bTickLODAnims=False
bAllowDynamicDecals=True
bAllowDynamicLights=True
bAllowDynamicShadows=True
bAllowLightEnvironmentShadows=True
bAllowStaticDecals=False
MaxNumberOfDynamicDecals=50
MaxNumberOfStaticDecals=0
MaxParticlesAllowed=700
ParticleCullExemptDistance = 4000
ParticleLODBias=2

[TextureLODSettings]
TEXTUREGROUP_Character=(MinLODSize=128,MaxLODSize=2048,LODBias=1)
TEXTUREGROUP_CharacterNormalMap=(MinLODSize=128,MaxLODSize=2048,LODBias=1)
TEXTUREGROUP_Effects=(MinLODSize=128,MaxLODSize=2048,LODBias=1)
TEXTUREGROUP_LightAndShadowMap=(MinLODSize=128,MaxLODSize=2048,LODBias=1)
TEXTUREGROUP_RenderTarget=(MinLODSize=1,MaxLODSize=2048,LODBias=1)
TEXTUREGROUP_Skybox=(MinLODSize=128,MaxLODSize=2048,LODBias=1)
TEXTUREGROUP_UI=(MinLODSize=256,MaxLODSize=4096,LODBias=0)
TEXTUREGROUP_Vehicle=(MinLODSize=128,MaxLODSize=2048,LODBias=1)
TEXTUREGROUP_VehicleNormalMap=(MinLODSize=128,MaxLODSize=2048,LODBias=1)
TEXTUREGROUP_Weapon=(MinLODSize=128,MaxLODSize=2048,LODBias=1)
TEXTUREGROUP_WeaponNormalMap=(MinLODSize=128,MaxLODSize=2048,LODBias=1)
TEXTUREGROUP_World=(MinLODSize=128,MaxLODSize=2048,LODBias=1)
TEXTUREGROUP_WorldNormalMap=(MinLODSize=128,MaxLODSize=2048,LODBias=1)

[WinDrv.WindowsClient]
StartupResolutionX=%s
StartupResolutionY=%s
StartupFullscreen=%s

[MOHAGame.MOHAScalabilityOptions]
bAllowBloom=True
bAllowDepthOfField=True
bAllowMotionBlur=False
bAllowStaticDecals=True
bMinspecCull=False
SkeletalMeshLODBias=1
StaticMeshLODBias=1
ScreenPercentage=100.0
bPostFX=True
bSimplePostFX=True
bGroupShadows=False
bForceFallbackShader=False
CullDistanceBiasBase=0.6

''' % (w,h,screen)
def highg():
    global screen
    global configfile
    global w
    global h
    configfile = '''
[ALAudio.ALAudioDevice]
MaxChannels=91
UseEffectsProcessing=True

[MOHAGame.MOHAScalabilityOptions]
bTickLODAnims=False
bAllowDynamicDecals=True
bAllowDynamicLights=True
bAllowDynamicShadows=True
bAllowLightEnvironmentShadows=True
bAllowStaticDecals=False
MaxNumberOfDynamicDecals=-1
MaxNumberOfStaticDecals=0
MaxParticlesAllowed=-1
ParticleCullExemptDistance = 0
ParticleLODBias=0

[TextureLODSettings]
TEXTUREGROUP_Character=(MinLODSize=256,MaxLODSize=4096,LODBias=0)
TEXTUREGROUP_CharacterNormalMap=(MinLODSize=256,MaxLODSize=4096,LODBias=0)
TEXTUREGROUP_Effects=(MinLODSize=256,MaxLODSize=4096,LODBias=0)
TEXTUREGROUP_LightAndShadowMap=(MinLODSize=256,MaxLODSize=4096,LODBias=0)
TEXTUREGROUP_RenderTarget=(MinLODSize=1,MaxLODSize=4096,LODBias=0)
TEXTUREGROUP_Skybox=(MinLODSize=256,MaxLODSize=4096,LODBias=0)
TEXTUREGROUP_UI=(MinLODSize=256,MaxLODSize=4096,LODBias=0)
TEXTUREGROUP_Vehicle=(MinLODSize=256,MaxLODSize=4096,LODBias=0)
TEXTUREGROUP_VehicleNormalMap=(MinLODSize=256,MaxLODSize=4096,LODBias=0)
TEXTUREGROUP_Weapon=(MinLODSize=256,MaxLODSize=4096,LODBias=0)
TEXTUREGROUP_WeaponNormalMap=(MinLODSize=256,MaxLODSize=4096,LODBias=0)
TEXTUREGROUP_World=(MinLODSize=256,MaxLODSize=4096,LODBias=0)
TEXTUREGROUP_WorldNormalMap=(MinLODSize=256,MaxLODSize=4096,LODBias=0)

[MOHAGame.MOHAScalabilityOptions]
bAllowBloom=True
bAllowDepthOfField=True
bAllowMotionBlur=True
bMinspecCull=False
SkeletalMeshLODBias=0
StaticMeshLODBias=0
ScreenPercentage=100.0
bPostFX=True
bSimplePostFX=False
bGroupShadows=False
bForceFallbackShader=False
CullDistanceBiasBase=1

[WinDrv.WindowsClient]
StartupResolutionX=%s
StartupResolutionY=%s
StartupFullscreen=%s
''' % (w,h,screen)
R3 = Radiobutton(root, text='Baixo', variable=var2, value=1,command=lowg)
R3.pack( anchor = W )
R4 = Radiobutton(root, text='Medio', variable=var2, value=2,command=medg)
R4.pack( anchor = W )
R5 = Radiobutton(root, text='Alto', variable=var2, value=3,command=highg)
R5.pack( anchor = W )

def create():
    global configfile
    with open('MOHASettings.ini', 'w') as f:
        f.write(configfile)
    root.destroy()

crea = Button(root, text ='Criar arquivo', command =create)
crea.pack()
        
root.mainloop()

