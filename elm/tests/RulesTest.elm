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
                            Rule.cellWillBeAlive True 0
                    in
                    Expect.equal False isAlive
            , test "cell should die with 1 neighbour" <|
                \_ ->
                    let
                        isAlive =
                            Rule.cellWillBeAlive True 1
                    in
                    Expect.equal False isAlive
            , test "cell should remain dead with 0 neighbours" <|
                \_ ->
                    let
                        isAlive =
                            Rule.cellWillBeAlive False 0
                    in
                    Expect.equal False isAlive
            , test "cell should remain dead with 1 neighbours" <|
                \_ ->
                    let
                        isAlive =
                            Rule.cellWillBeAlive False 1
                    in
                    Expect.equal False isAlive
            ]
        , describe "survival"
            [ test "cell should survive with 2 neighbours" <|
                \_ ->
                    let
                        isAlive =
                            Rule.cellWillBeAlive True 2
                    in
                    Expect.equal True isAlive
            , test "cell should survive with 3 neighbours" <|
                \_ ->
                    let
                        isAlive =
                            Rule.cellWillBeAlive True 3
                    in
                    Expect.equal True isAlive
            , test "cell should remain dead with 2 neighbours" <|
                \_ ->
                    let
                        isAlive =
                            Rule.cellWillBeAlive False 2
                    in
                    Expect.equal False isAlive
            ]
        , describe "revival"
            [ test "cell should come alive with 3 neighbours" <|
                \_ ->
                    let
                        isAlive =
                            Rule.cellWillBeAlive False 3
                    in
                    Expect.equal True isAlive
            ]
        ]
