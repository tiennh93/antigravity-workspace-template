# 🪐 Plantilla de Workspace de Google Antigravity

**Kit inicial de nivel producción para agentes de IA autónomos en Google Antigravity.**

Idioma: [English](/docs/en/) | [中文](README_CN.md) | [Español](/docs/es/)

![License](https://img.shields.io/badge/License-MIT-green)
![Gemini](https://img.shields.io/badge/AI-Gemini_2.0_Flash-blue)
![Architecture](https://img.shields.io/badge/Architecture-Event_Driven-purple)
![Memory](https://img.shields.io/badge/Context-Infinite-orange)

## 🌟 Intención del Proyecto

En un mundo lleno de IDEs de IA, quiero que la arquitectura de nivel empresarial sea tan simple como **Clonar → Renombrar → Solicitar**.

Este proyecto aprovecha la conciencia de contexto del IDE (mediante `.cursorrules` y `.antigravity/rules.md`) para preincrustar una **arquitectura cognitiva** completa en el repositorio.

Cuando abres este proyecto, tu IDE deja de ser solo un editor y se convierte en un **arquitecto que entiende el negocio**.

**Primeros principios:**

- **Minimizar la repetición**: el repositorio debe codificar valores por defecto para que la puesta en marcha sea casi nula.
- **Expresar la intención de forma explícita**: captura arquitectura, contexto y flujos de trabajo en archivos, no en conocimiento tácito.
- **Tratar el IDE como compañero**: las reglas contextuales convierten al editor en un arquitecto proactivo, no en una herramienta pasiva.

### ¿Por qué necesitamos un andamio que piense?

Al trabajar con Google Antigravity o Cursor, descubrí un punto de dolor:

**El IDE y los modelos son potentes, pero el proyecto vacío es demasiado débil.**

Cada proyecto nuevo repite la misma configuración aburrida:

- "¿Debo poner el código en `src` o en `app`?"
- "¿Cómo defino utilidades para que Gemini las reconozca?"
- "¿Cómo ayudo a la IA a recordar el contexto previo?"

Esta repetición desperdicia energía creativa. Mi flujo ideal es: **después de un git clone, el IDE ya sabe qué hacer.**

Así que construí este proyecto: **Antigravity Workspace Template**.

## ⚡ Inicio Rápido

### Opción A: pip install (recomendado)

```bash
pip install antigravity-agent
antigravity init my-project
cd my-project
```

### Opción B: Clonar plantilla

```bash
git clone https://github.com/study8677/antigravity-workspace-template.git my-project
cd my-project
```

### Instalación automática (configuración completa)

**Linux / macOS:**
```bash
# 1. Clona la plantilla
git clone https://github.com/study8677/antigravity-workspace-template.git mi-proyecto
cd mi-proyecto

# 2. Ejecuta el instalador
chmod +x install.sh
./install.sh

# 3. Configura tus claves de API
nano .env

# 4. Ejecuta el agente
source venv/bin/activate
python src/agent.py
```

**Windows:**
```cmd
# 1. Clona la plantilla
git clone https://github.com/study8677/antigravity-workspace-template.git mi-proyecto
cd mi-proyecto

# 2. Ejecuta el instalador
install.bat

# 3. Configura tus claves de API (notepad .env)

# 4. Ejecuta el agente
python src/agent.py
```

### Instalación manual

```bash
# 1. Clona la plantilla
git clone https://github.com/study8677/antigravity-workspace-template.git mi-proyecto
cd mi-proyecto

# 2. Crea un entorno virtual
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 3. Instala dependencias
pip install -r requirements.txt

# 4. Configura tus claves de API
cp .env.example .env  # (si existe) o crea .env manualmente
nano .env

# 5. Ejecuta el agente
python src/agent.py
```

**Eso es todo.** El IDE carga la configuración automáticamente vía `.cursorrules` + `.antigravity/rules.md`. Ya puedes empezar a pedir.

## 🎯 ¿Qué es esto?

Esto **no** es otro wrapper de LangChain. Es un workspace mínimo y transparente para construir agentes de IA que:

- 🧠 Tienen memoria infinita (resumización recursiva)
- 🛠️ Descubren herramientas automáticamente desde `src/tools/`
- 📚 Inyectan contexto automáticamente desde `.context/`
- 🔌 Se conectan a servidores MCP sin fricción
- 🤖 Coordinan múltiples agentes especialistas
- 📦 Guardan salidas como artefactos (planes, logs, evidencia)

**Clonar → Renombrar → Solicitar. Ese es el flujo de trabajo.**

## 🚀 Características clave

| Característica | Descripción |
|---------|-------------|
| 🧠 **Memoria infinita** | La resumización recursiva comprime el contexto automáticamente |
| 🧠 **Pensamiento Real** | Paso de "Deep Think" (Chain-of-Thought) antes de actuar |
| 🎓 **Sistema de Habilidades** | Capacidades modulares como carpetas (`src/skills/`) con carga automática (incluye `agent-repo-init`) |
| 🛠️ **Herramientas universales** | Coloca funciones Python en `src/tools/` → se descubren solas |
| 📚 **Contexto automático** | Agrega archivos a `.context/` → se inyectan en los prompts |
| 🔌 **Soporte MCP** | Conecta GitHub, bases de datos, sistemas de archivos, servidores personalizados |
| 🤖 **Agentes Swarm** | Orquestación multiagente con patrón Router-Worker |
| ⚡ **Nativo de Gemini** | Optimizado para Gemini 2.0 Flash |
| 🌐 **Independiente del LLM** | Usa OpenAI, Azure, Ollama o cualquier API compatible con OpenAI |
| 📂 **Artifact-First** | Flujo de trabajo por convención para guardar planes, logs y evidencia en `artifacts/` |

## 📚 Documentación

**Documentación completa disponible en `/docs/en/`:**

- **[Quick Start](docs/en/QUICK_START.md)** — Instalación y despliegue
- **[Philosophy](docs/en/PHILOSOPHY.md)** — Conceptos y arquitectura
- **[Zero-Config](docs/en/ZERO_CONFIG.md)** — Carga automática de herramientas y contexto
- **[MCP Integration](docs/en/MCP_INTEGRATION.md)** — Conectividad con herramientas externas
- **[Swarm Protocol](docs/en/SWARM_PROTOCOL.md)** — Coordinación multiagente
- **[Roadmap](docs/en/ROADMAP.md)** — Fases futuras y visión

## 🏗️ Estructura del proyecto

```
src/
├── agent.py           # Bucle principal del agente
├── memory.py          # Gestor de memoria JSON
├── mcp_client.py      # Integración de MCP
├── swarm.py           # Orquestación multiagente
├── agents/            # Agentes especialistas
├── tools/             # Tus herramientas personalizadas
└── skills/            # Habilidades modulares (Zero-Config)

.context/             # Base de conocimiento (auto-inyectada)
.antigravity/         # Reglas de Antigravity
artifacts/            # Salidas y evidencia
```

## 💡 Ejemplo: construir una herramienta en 30 segundos

```python
# src/tools/my_tool.py
def analyze_sentiment(text: str) -> str:
    """Analiza el sentimiento del texto dado."""
    return "positive" if len(text) > 10 else "neutral"
```

**Reinicia el agente.** ¡Listo! La herramienta ya está disponible.

## 🎓 Ejemplo: inicializar un nuevo repositorio con skill

La skill integrada `agent-repo-init` soporta dos modos:
- `quick`: scaffold limpio mínimo
- `full`: scaffold + perfil de runtime (`.env`, mission, perfil de contexto e informe)

Puedes usar el script portable en `skills/agent-repo-init/scripts/init_project.py`:

```text
python skills/agent-repo-init/scripts/init_project.py \
  --project-name my-new-agent \
  --destination-root /absolute/path/for/new/projects \
  --mode quick
```

Ejemplo de `full` mode:

```text
python skills/agent-repo-init/scripts/init_project.py \
  --project-name my-new-agent \
  --destination-root /absolute/path/for/new/projects \
  --mode full --llm-provider openai --enable-mcp --disable-swarm --enable-docker --init-git
```

## 🔌 Integración de MCP

Conecta herramientas externas:

```json
{
  "servers": [
    {
      "name": "github",
      "transport": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "enabled": true
    }
  ]
}
```

El agente descubre y usa automáticamente todas las herramientas MCP.

## 🤖 Swarm multiagente

Descompón tareas complejas:

```python
from src.swarm import SwarmOrchestrator

swarm = SwarmOrchestrator()
result = swarm.execute("Construir y revisar una calculadora")
```

El swarm automáticamente:
- 📤 Enruta a los agentes Coder, Reviewer y Researcher
- 🧩 Sintetiza resultados
- 📂 Expone logs de mensajes vía `get_message_log()` para inspección

## ✅ Qué está completo

- ✅ Fases 1-7: Foundation, DevOps, Memory, Tools, Swarm, Discovery
- ✅ Fase 8: Integración de MCP (totalmente implementada)
- 🚀 Fase 9: Enterprise Core (en progreso)

## 🆕 Actualizaciones recientes

- Añadido **Pensamiento Real (True Thinking)**: El agente realiza un paso real de "Deep Think" (CoT) antes de cada acción, generando un plan estructurado.
- Añadido **Sistema de Habilidades (Skills System)**: Nuevo directorio `src/skills/` permite capacidades modulares basadas en carpetas (Docs + Código).
- Añadida **skill agent-repo-init**: Inicializa un repositorio limpio y reutilizable desde esta plantilla con `init_agent_repo`.
- Soporte para backend local compatible con OpenAI (p.ej., Ollama) cuando no hay clave de Google.
- Corrección de carga de `.env`: ejecutar desde `src/` sigue leyendo la configuración en la raíz del proyecto.
- Los entrypoints ahora aceptan tareas por argumentos `AGENT_TASK`.

Consulta la [Hoja de Ruta](docs/en/ROADMAP.md) para más detalles.

## 🤝 Contribuyendo

¡Las ideas también cuentan como contribuciones! Abre un [issue](https://github.com/study8677/antigravity-workspace-template/issues) para:
- Reportar bugs
- Sugerir funcionalidades
- Proponer arquitectura (Fase 9)

O envía un PR para mejorar documentación o código.

## 👥 Contribuidores

- [@devalexanderdaza](https://github.com/devalexanderdaza) — Primer contribuidor. Implementó herramientas de demostración, mejoró la funcionalidad del agente, propuso la hoja de ruta "Agent OS" y completó la integración MCP.
- [@Subham-KRLX](https://github.com/Subham-KRLX) — Añadió carga dinámica de herramientas y contexto (Fixes #4) y el protocolo de clúster multiagente (Fixes #6).

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=study8677/antigravity-workspace-template&type=Date)](https://star-history.com/#study8677/antigravity-workspace-template&Date)

## 📄 Licencia

Licencia MIT. Ver [LICENSE](LICENSE) para detalles.

---

**[Explorar documentación completa →](docs/en/)**
