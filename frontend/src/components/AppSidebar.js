import {
    Sidebar,
    SidebarContent,
    SidebarGroup,
    SidebarGroupContent,
    SidebarGroupLabel,
    SidebarMenu,
    SidebarMenuButton,
    SidebarMenuItem,
    SidebarHeader,
    SidebarFooter,
  } from "@/components/ui/sidebar";
  
  // Import HeroIcons
  import { HomeIcon, RocketLaunchIcon, AcademicCapIcon, BeakerIcon, CalendarIcon } from "@heroicons/react/24/outline";
  
  // Menu items with HeroIcons
  const items = [
    {
      title: "Home",
      url: "#",
      icon: HomeIcon,
    },
    {
      title: "Launchpad",
      url: "#",
      icon: RocketLaunchIcon,
    },
    {
      title: "Internships",
      url: "#",
      icon: AcademicCapIcon,
    },
    {
      title: "Research",
      url: "#",
      icon: BeakerIcon,
    },
    {
      title: "Events",
      url: "#",
      icon: CalendarIcon,
    },
  ];
  
  export function AppSidebar() {
    return (
      <Sidebar>
        <SidebarHeader />
        <SidebarContent>
          <SidebarGroup>
            <SidebarGroupLabel>Application</SidebarGroupLabel>
            <SidebarGroupContent>
              <SidebarMenu>
                {items.map((item) => (
                  <SidebarMenuItem key={item.title}>
                    <SidebarMenuButton asChild>
                      <a href={item.url} className="flex items-center space-x-2">
                        {/* Render Icon */}
                        <item.icon className="h-5 w-5 text-gray-500" />
                        {/* Render Title */}
                        <span>{item.title}</span>
                      </a>
                    </SidebarMenuButton>
                  </SidebarMenuItem>
                ))}
              </SidebarMenu>
            </SidebarGroupContent>
          </SidebarGroup>
        </SidebarContent>
        <SidebarFooter />
      </Sidebar>
    );
  }
  