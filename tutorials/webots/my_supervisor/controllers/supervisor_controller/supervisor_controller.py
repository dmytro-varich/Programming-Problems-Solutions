from controller import Supervisor

TIME_STEP = 32

robot = Supervisor()  # create Supervisor instance

bb8_node = robot.getFromDef('BB-8')
translation_field = bb8_node.getField('translation')

root_node = robot.getRoot()
children_field = root_node.getField('children')

children_field.importMFNodeFromString(-1, 'DEF BALL Ball { translation 0 1 1 }')
ball_node = robot.getFromDef('BALL')
color_field = ball_node.getField('color')

i = 0
while robot.step(TIME_STEP) != -1:
    if i == 0:
        new_value = [2.5, 0, 0]
        translation_field.setSFVec3f(new_value)
    
    if i == 10:
        bb8_node.remove()
    
    if i == 20:
        children_field.importMFNodeFromString(-1, 'Nao { translation 2.5 0 0.334 }')  # -1 is position, where we want to paste the node, that is, in the last row of nodes. 'Nao { }'  is a string that describes what we wish to spawn.         
    
    
    position = ball_node.getPosition()
    print('Ball position: %f %f %f\n' %(position[0], position[1], position[2]))
    
    if position[2] < 0.2:
        red_color = [1, 0, 0]
        color_field.setSFColor(red_color)
    
    i += 1 