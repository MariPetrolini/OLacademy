#include <limits.h>
#include <mach-o/dyld.h>
#include <spawn.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/wait.h>

extern char **environ;

int main(void) {
  char executable[PATH_MAX];
  uint32_t size = sizeof(executable);
  if (_NSGetExecutablePath(executable, &size) != 0) return 1;

  char *separator = strrchr(executable, '/');
  if (separator == NULL) return 1;
  *separator = '\0';

  char launcher[PATH_MAX];
  int written = snprintf(launcher, sizeof(launcher), "%s/../Resources/launcher.sh", executable);
  if (written < 0 || (size_t)written >= sizeof(launcher)) return 1;

  char *arguments[] = {"/bin/zsh", launcher, NULL};
  pid_t child;
  int result = posix_spawn(&child, "/bin/zsh", NULL, NULL, arguments, environ);
  if (result != 0) return result;

  int status;
  if (waitpid(child, &status, 0) < 0) return 1;
  return WIFEXITED(status) ? WEXITSTATUS(status) : 1;
}
