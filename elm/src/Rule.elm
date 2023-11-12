module Rule exposing (cellWillBeAlive)


cellWillBeAlive : Int -> Bool
cellWillBeAlive neighbours =
    if neighbours == 2 || neighbours == 3 then
        True

    else
        False
