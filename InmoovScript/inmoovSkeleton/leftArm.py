# ##############################################################################
#            *** LEFT ARM ***
# ##############################################################################

  
  
# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current skeleton part config
isLeftArmActivated=0
ThisSkeletonPart=inspect.getfile(inspect.currentframe()).replace('.py','')

###############################################################################
#                 webgui sync
getInmoovFrParameter('leftArm',ThisSkeletonPart+'.config')
###############################################################################

try:
  CheckFileExist(ThisSkeletonPart)
  ThisSkeletonPartConfig = ConfigParser.ConfigParser()
  ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')
  isLeftArmActivated=ThisSkeletonPartConfig.getboolean('MAIN', 'isLeftArmActivated') 
  

except:
  errorSpokenFunc('ConfigParserProblem','leftarm.config')
  pass
  
# ##############################################################################
#                 SERVO FUNCTIONS
# ##############################################################################

if isLeftArmActivated==1 and (ScriptType=="LeftSide" or ScriptType=="Full" or ScriptType=="Virtual"):
  if LeftPortIsConnected==True:
    talkEvent(lang_startingLeftArm)
    
    leftArm = Runtime.create("i01.leftArm", "InMoovArm")
    
    try:      
      leftArm.bicep.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'bicep'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'bicep'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'bicep'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'bicep')) 
      leftArm.shoulder.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'shoulder'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'shoulder'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'shoulder'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'shoulder')) 
      leftArm.rotate.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'rotate'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'rotate'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'rotate'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'rotate')) 
      leftArm.omoplate.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'omoplate'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'omoplate'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'omoplate'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'omoplate')) 
      
      leftArm.bicep.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'bicep'))
      leftArm.shoulder.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'shoulder'))
      leftArm.rotate.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'rotate'))
      leftArm.omoplate.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'omoplate'))
      
      leftArm.bicep.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'bicep'))
      leftArm.shoulder.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'shoulder'))
      leftArm.rotate.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'rotate'))
      leftArm.omoplate.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'omoplate'))
    except:
      errorSpokenFunc('ConfigParserProblem',ThisSkeletonPart)
      pass
      
    if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'bicep'):
      leftArm.bicep.setInverted(True)
    if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'shoulder'):
      leftArm.shoulder.setInverted(True)
    if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'rotate'):
      leftArm.rotate.setInverted(True)
    if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'omoplate'):
      leftArm.omoplate.setInverted(True)
    
    i01.startLeftArm(MyLeftPort)
    
    leftArm.enableAutoEnable(1)
    leftArm.enableAutoEnable(0)
    
    leftArm.rest()

  else:
    #we force parameter if arduino is off
    isLeftArmActivated=0
    
#todo set inverted
