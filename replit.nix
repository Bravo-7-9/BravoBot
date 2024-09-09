{ pkgs }: {
  deps = [
    pkgs.run
    pkgs.nodePackages.prettier
  ];
  env = {
  };
}