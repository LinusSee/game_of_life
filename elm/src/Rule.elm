module Rule exposing (cellWillBeAlive)


cellWillBeAlive : Int -> Bool
cellWillBeAlive neighbours =
    if neighbours == 2 then
        True

    else
        False
