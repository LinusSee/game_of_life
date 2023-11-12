module Rule exposing (cellWillBeAlive)


cellWillBeAlive : Bool -> Int -> Bool
cellWillBeAlive isAlive neighbours =
    if neighbours == 2 && isAlive || neighbours == 3 then
        True

    else
        False
