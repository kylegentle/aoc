{
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/release-24.11";

  outputs =
    { nixpkgs, ... }@inputs:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        packages = with pkgs; [
          cargo
          pyright
          python3
          ruff
          rustc
        ];
      };
    };
}
