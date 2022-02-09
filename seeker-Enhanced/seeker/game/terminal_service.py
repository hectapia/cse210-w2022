class TerminalService:
    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """
     
    def read_text(self, prompt):
        """Gets text input from the terminal. Directs the user with the given prompt.

        Args: 
           self (TerminalService): An instance of TerminalService.
           prompt (string): The prompt to display on the terminal.

        Returns:
           string: The user's input as text.
        """
        return input(prompt)
    

   
    def read_number(self, prompt):
        """Gets numerical input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            float: The user's input as a number.
        """
       

        # ######################################################################
        # Chages added by Hector Olivares Tapia as result of cse210 assignment #
        # ######################################################################

       #Enhanced input validation.
        print_error = "Oops!  That was no valid entranced.  Try again..."

        control_error = True
        while control_error:
            try:
                location = float(input(prompt))
                
                control_error = (location < 1 or location > 1000) 
                if control_error:  
                 self.write_text(print_error) 
            except ValueError:
                self.write_text(print_error)

        return location
        
    def write_text(self, text):
        """Displays the given text on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
            text (string): The text to display.
        """
        print(text)