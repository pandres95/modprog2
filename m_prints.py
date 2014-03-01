import color_console as cons
import sys

def m_print(m, c_end = '\t', r_end='\n'):
    
    default_colors = cons.get_text_attr()
    default_bg = default_colors & 0x0070
    default_fg = default_colors & 0x0007
    
    for i in m:
        for j in i:
            if(j == 1):
                sys.stdout.flush() # Force writing first part of the line in blue  
                cons.set_text_attr(cons.FOREGROUND_RED | cons.BACKGROUND_GREY | cons.FOREGROUND_INTENSITY | cons.BACKGROUND_INTENSITY)                
            elif(j == 2):
                sys.stdout.flush() # Force writing first part of the line in blue  
                cons.set_text_attr(cons.FOREGROUND_YELLOW | cons.BACKGROUND_RED | cons.FOREGROUND_INTENSITY | cons.BACKGROUND_INTENSITY)
            else:
                sys.stdout.flush() # Force writing first part of the line in blue  
                cons.set_text_attr(default_colors)
            print(j, end=c_end)
        print(end=r_end)