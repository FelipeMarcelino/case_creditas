# shell.nix
let
  # We pin to a specific nixpkgs commit for reproducibility.
  # Last updated: 2024-08-07. Check for new commits at https://status.nixos.org.
  pkgs = import (fetchTarball "https://github.com/NixOS/nixpkgs/archive/cf8cc1201be8bc71b7cbbbdaf349b22f4f99c7ae.tar.gz") {};
in
  pkgs.mkShell {
    packages = [
      (pkgs.python311.withPackages (python-pkgs: [
        # select Python packages here
        python-pkgs.pandas
        python-pkgs.requests
        python-pkgs.seaborn
        python-pkgs.xgboost
        python-pkgs.lightgbm
        python-pkgs.jupyter
        python-pkgs.scikit-learn
        python-pkgs.shap
        python-pkgs.optuna
        python-pkgs.pip
      ]))
      pkgs.pandoc
      pkgs.texliveFull
      pkgs.texlivePackages.tcolorbox
    ];
  }
