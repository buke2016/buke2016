    n=coffees.pygame.BufferProxy.length
            i = 1
            while i < n:
                while coffees[i-1].fresh>coffees[i].fresh:
                    #swap places
                    i += 1