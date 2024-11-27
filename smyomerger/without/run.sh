#!/bin/csh

source /usr/local/gromacs/bin/GMXRC

# Minimization
setenv GMX_MAXCONSTRWARN -1

# step4.0 - soft-core minimization
gmx grompp -f step4.0_minimization.mdp -o step4.0_minimization.tpr -c step3_charmm2gmx.pdb -r step3_charmm2gmx.pdb -p system.top -n index.ndx
gmx mdrun -deffnm step4.0_minimization -nt 1

# step4.1
gmx grompp -f step4.1_minimization.mdp -o step4.1_minimization.tpr -c step4.0_minimization.gro -r step3_charmm2gmx.pdb -p system.top -n index.ndx
gmx mdrun -deffnm step4.1_minimization -nt 1
unsetenv GMX_MAXCONSTRWARN

# Equilibration
gmx grompp -f step4.2_equilibration.mdp -o step4.2_equilibration.tpr -c step4.1_minimization.gro -r step3_charmm2gmx.pdb -p system.top -n index.ndx -maxwarn 1
gmx mdrun -deffnm step4.2_equilibration -v -nt 4

# Production
gmx grompp -f step5_production.mdp -o step5_production.tpr -c step4.2_equilibration.gro -p system.top -n index.ndx
gmx mdrun -deffnm step5_production -v -nt 4

