## install homebrew
echo "Installing Homebrew.."
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/$USER/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
echo "Homebrew successfully installed"

## install git
echo "Installing git.."
brew install git
echo "git successfully installed"

## install ripgrep
echo "Installing ripgrep..."
brew install ripgrep
echo "ripgrep installed"

## install git completion
echo "Installing git completion.."
curl https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash > ~/.git-completion.bash
echo "git completion successfully installed"

## install iterm2
echo "Installing iTerm2.."
cd ~/Downloads
curl https://iterm2.com/downloads/stable/iTerm2-3_1_7.zip > iTerm2.zip
unzip iTerm2.zip &> /dev/null
mv iTerm.app/ /Applications/iTerm.app
spctl --add /Applications/iTerm.app
rm -rf iTerm2.zip
echo "iTerm2 successfully installed.."

## install oh-my-zsh
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

## install visual studio code
echo "Installing VS Code.."
brew install visual-studio-code
## this might ask you for your password
code --version
echo "VS Code successfully installed"

## install tldr https://tldr.sh/
echo "Installing tldr..."
brew install tldr
echo "tldr installed. "

## install bash completion
echo "Installing bash completion.."
brew install bash-completion
echo "bash completion successfully installed"

## update terminal prompt
echo "Updating terminal prompt.."
curl https://raw.githubusercontent.com/git/git/master/contrib/completion/git-prompt.sh >> ~/.git-prompt.sh
echo "Terminal prompt successfully updated"

## create global gitignore
echo "Creating a global gitignore.."
git config --global core.excludesfile ~/.gitignore
touch ~/.gitignore
echo '.DS_Store' >> ~/.gitignore
echo '.idea' >> ~/.gitignore
echo "Global gitignore created"

## install dbt
echo "Installing dbt.."
brew update
brew tap fishtown-analytics/dbt
brew install dbt
echo "dbt successfully installed.. Printing version.."
dbt --version
echo "Setting up dbt profile.."
mkdir ~/.dbt
touch ~/.dbt/profiles.yml
curl  path/to/profiles.yml >> ~/.dbt/profiles.yml
echo "dbt profile created.. You will need to edit this file later."

## install the dbt completion script
echo "Installing dbt completion script.."
curl https://raw.githubusercontent.com/fishtown-analytics/dbt-completion.bash/master/dbt-completion.bash > ~/.dbt-completion.bash
echo "dbt completion script successfully installed"
