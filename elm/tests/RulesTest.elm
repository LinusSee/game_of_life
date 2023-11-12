module RulesTest exposing (..)

import Expect
import Rule
import Test exposing (..)


rulesSuite : Test
rulesSuite =
    describe "Testing GameOfLifeRules"
        [ describe "underpopulation"
            [ test "cell should die with 0 neighbours" <|
                \_ ->
                    let
                        isAlive =
                            Rule.cellWillBeAlive 0
                    in
                    Expect.equal False isAlive
            , test "cell should die with 1 neighbour" <|
                \_ ->
                    let
                        isAlive =
                            Rule.cellWillBeAlive 1
                    in
                    Expect.equal False isAlive
            ]
        ]
