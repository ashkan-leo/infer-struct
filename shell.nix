{ pkgs ? import <nixpkgs> { } }:

let
  # projectEnv = pkgs.poetry2nix.mkPoetryEnv { projectDir = ./.; };
  dependencies = with pkgs; [ nodePackages.pyright  python39Packages.poetry ];
in pkgs.mkShell {
  buildInputs = [ dependencies ];
  # shellHook = "poetry shell";
}
